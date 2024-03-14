import requests


def get_pokemon_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from API")
        return None


def get_fast_growth_pokemon(generation_name):
    weighted_moves_multiplier = 10
    fast_growth_pokemon = []
    for i in range(1, 899):  # Assuming there are 898 Pokémon in the API
        pokemon_data = get_pokemon_data(f"https://pokeapi.co/api/v2/pokemon-species/{i}/")
        if pokemon_data:
            print(pokemon_data['name'])
            growth_rate = pokemon_data['growth_rate']['name']
            if growth_rate == 'fast':  # Change this condition if you want different growth rates
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
        return base_stat_total
    else:
        return 0


def find_highest_base_stat_total(fast_growth_pokemon):
    max_base_stat_total = 0
    best_pokemon = ''
    total_calculated_value = 0
    for pokemon in fast_growth_pokemon:
        base_stat_total = get_base_stat_total(pokemon["name"])
        calculated_value = base_stat_total + pokemon["weighted_value"]
        if calculated_value > total_calculated_value:
            max_base_stat_total = base_stat_total
            total_calculated_value = calculated_value
            best_pokemon = pokemon["name"]
        elif total_calculated_value == calculated_value:
            print(f"Score tie between '{best_pokemon}' and '{pokemon["name"]}' with a BST of '{base_stat_total}' "
                  f"and total calculated value of '{calculated_value}'.")
    return best_pokemon, max_base_stat_total, total_calculated_value


if __name__ == "__main__":
    # Options for generation name are:
    # yellow, red-blue, gold-silver, crystal, ruby-sapphire, emerald, firered-leafgreen, etc
    generation_name = "emerald"
    fast_growth_pokemon = get_fast_growth_pokemon(generation_name)
    if fast_growth_pokemon:
        best_pokemon, max_base_stat_total, total_calculated_value = find_highest_base_stat_total(fast_growth_pokemon)
        print(f"The Pokémon with the highest score among fast growth rate Pokémon is: {best_pokemon}")
        print(f"Base stat total: {max_base_stat_total}")
        print(f"Total score: '{total_calculated_value}'")
    else:
        print("No fast growth rate Pokémon found that learn moves by leveling up.")
