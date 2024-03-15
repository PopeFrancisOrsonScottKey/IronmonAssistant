import requests


def get_pokemon_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from API")
        return None


def get_fast_growth_pokemon(generation_name, desired_growth_rate):
    weighted_moves_multiplier = 10
    fast_growth_pokemon = []
    for i in range(1, 400):  # Assuming there are 898 Pokémon in the API
        pokemon_data = get_pokemon_data(f"https://pokeapi.co/api/v2/pokemon-species/{i}/")
        if pokemon_data:
            print(pokemon_data['name'])
            growth_rate = pokemon_data['growth_rate']['name']
            if growth_rate == desired_growth_rate or not growth_rate:
                weighted_moves_value = learns_moves_by_leveling_up(pokemon_data['id'], generation_name) * weighted_moves_multiplier
                fast_growth_pokemon.append({"name": pokemon_data['name'], "weighted_value": weighted_moves_value})
    return fast_growth_pokemon


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
    print(count)
    return count


def get_base_stat_total(pokemon_name):
    pokemon_data = get_pokemon_data(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")
    if pokemon_data:
        base_stats = pokemon_data['stats']
        base_stat_total = sum(stat['base_stat'] for stat in base_stats)
        if base_stat_total >= 600:
            print(f"'{pokemon_name}' is excluded due to having too high of a BST- '{base_stat_total}'.")
            return 0
        return base_stat_total
    return 0


def find_highest_base_stat_total(fast_growth_pokemon):
    best_pokemon = []
    for pokemon in fast_growth_pokemon:
        base_stat_total = get_base_stat_total(pokemon["name"])
        calculated_value = base_stat_total + pokemon["weighted_value"]
        best_pokemon.append({"name": pokemon["name"], "bst": base_stat_total, "calculated_value": calculated_value})
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
    growth_rate = "fast"
    fast_growth_pokemon = get_fast_growth_pokemon(generation_name, growth_rate)
    if fast_growth_pokemon:
        top_ten_pokemon = find_highest_base_stat_total(fast_growth_pokemon)
        place = 10
        for pokemon in top_ten_pokemon:
            print(f"At number '{place}' is '{pokemon["name"]}'")
            print(f"Base stat total: {pokemon["bst"]}")
            print(f"Total score: '{pokemon["calculated_value"]}'\n")
            place -= 1
    else:
        print("No fast growth rate Pokémon found that learn moves by leveling up.")
