import requests

from typeResistances import get_dual_type, calculate_defensive_score, get_type_stats_from_name


def get_pokemon_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from API")
        return None


def get_pokemon_by_growth(generation_name, desired_growth_rate):
    weighted_moves_multiplier = 10
    pokemon_by_growth = []
    for i in range(1, 899):  # Assuming there are 898 Pokémon in the API
        pokemon_data = get_pokemon_data(f"https://pokeapi.co/api/v2/pokemon-species/{i}/")
        if pokemon_data:
            growth_rate = pokemon_data['growth_rate']['name']
            if growth_rate == desired_growth_rate or not desired_growth_rate:
                weighted_moves_value = learns_moves_by_leveling_up(pokemon_data['id'], generation_name) * weighted_moves_multiplier
                pokemon_by_growth.append({"name": pokemon_data['name'], "weighted_value": weighted_moves_value})
    return pokemon_by_growth


def check_all_learn_methods(move_detail, generation_name):
    for detail in move_detail['version_group_details']:
        if (detail['move_learn_method']['name'] == 'level-up' and
                detail['level_learned_at'] > 1 and
                detail['version_group']['name'] == generation_name):
            return 1
    return 0


def learns_moves_by_leveling_up(pokemon_id, generation_name):
    moves_data = get_pokemon_data(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/")
    count = 0
    if moves_data:
        for move in moves_data['moves']:
            if 'version_group_details' in move:
                count += check_all_learn_methods(move, generation_name)
    return count


def get_type_score(type_block):
    if len(type_block) == 2:
        combined_type_block = get_dual_type(type_block[0]["type"]["name"], type_block[1]["type"]["name"])
    else:
        combined_type_block = get_type_stats_from_name(type_block[0]["type"]["name"])
    return calculate_defensive_score(combined_type_block)


def weigh_type_score(type_score, immunities, weakness_score):
    resistance_and_weakness_score = ((type_score / (type_score + 5)) * 100)
    immunity_score = (25 * immunities)
    weakness_score = ((weakness_score / (weakness_score + .05)) * 20)
    if resistance_and_weakness_score > weakness_score:
        return resistance_and_weakness_score + immunity_score - weakness_score
    return immunity_score


def get_base_stat_total(pokemon_name):
    pokemon_data = get_pokemon_data(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")
    if pokemon_data:
        type_score, immunities, weakness_score = get_type_score(pokemon_data["types"])
        weighted_type_score = weigh_type_score(type_score, immunities, weakness_score)
        base_stats = pokemon_data['stats']
        base_stat_total = sum(stat['base_stat'] for stat in base_stats)
        if base_stat_total >= 600:
            print(f"This pokemon's BST exceeds the allowed BST. You may evolve into it, but you cannot choose it - {pokemon_data["name"]}")
            return 0, 0
        return base_stat_total, weighted_type_score
    return 0, 0


def find_highest_base_stat_total(filter_pokemon):
    best_pokemon = []
    for pokemon in filter_pokemon:
        base_stat_total, typing_score = get_base_stat_total(pokemon["name"])
        print(f"{pokemon["name"]} has base stat total of {base_stat_total} and weighted move value of {pokemon["weighted_value"]} and typing score of {typing_score}")
        calculated_value = base_stat_total + pokemon["weighted_value"] + typing_score
        best_pokemon.append({"name": pokemon["name"], "bst": base_stat_total, "calculated_value": int(calculated_value)})
        best_pokemon = sorted(best_pokemon, key=lambda x: x["calculated_value"])
        if len(best_pokemon) > 10:
            best_pokemon.pop(0)
    return best_pokemon


if __name__ == "__main__":
    # Options for generation name are:
    # yellow, red-blue, gold-silver, crystal, ruby-sapphire, emerald, firered-leafgreen, etc
    generation_name = "emerald"
    # Set growth rate to look for. If you don't want to filter by growth rate, then leave this blank
    # Options for growth rate are:
    # slow, medium-slow, medium, fast (This seems to be different from what's listed on bulbapedia)
    growth_rate = ""
    filtered_pokemon = get_pokemon_by_growth(generation_name, growth_rate)
    if filtered_pokemon:
        top_ten_pokemon = find_highest_base_stat_total(filtered_pokemon)
        place = 10
        for pokemon in top_ten_pokemon:
            print(f"At number '{place}' is '{pokemon["name"]}'")
            print(f"Base stat total: {pokemon["bst"]}")
            print(f"Total score: '{pokemon["calculated_value"]}'\n")
            place -= 1
    else:
        print("No Pokémon found that learn moves by leveling up.")
