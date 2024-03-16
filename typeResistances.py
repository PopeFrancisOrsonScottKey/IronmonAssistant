def get_dual_type(type1_name, type2_name):
    dual_type = []
    type1 = get_type_stats_from_name(type1_name)
    type2 = get_type_stats_from_name(type2_name)
    for typeIdx in range(len(type1)):
        dual_type.append(
            {"type": type1[typeIdx]["type"], "resistance": type1[typeIdx]["resistance"] * type2[typeIdx]["resistance"]})
    return dual_type


def calculate_defensive_score(types):
    weakness_score = 1
    ongoing_score = 1
    immunities = 0
    for type in types:
        if type["resistance"] != 0:
            ongoing_score *= 1 / type["resistance"]
            if type["resistance"] < 1:
                weakness_score *= type["resistance"]
        else:
            immunities += 1
    return ongoing_score, immunities, weakness_score


def get_normal_type_defenses():
    return [{"type": "normal", "resistance": 1},
            {"type": "fire", "resistance": 1},
            {"type": "water", "resistance": 1},
            {"type": "electric", "resistance": 1},
            {"type": "grass", "resistance": 1},
            {"type": "ice", "resistance": 1},
            {"type": "fighting", "resistance": 2},
            {"type": "poison", "resistance": 1},
            {"type": "ground", "resistance": 1},
            {"type": "flying", "resistance": 1},
            {"type": "psychic", "resistance": 1},
            {"type": "bug", "resistance": 1},
            {"type": "rock", "resistance": 1},
            {"type": "ghost", "resistance": 0},
            {"type": "dragon", "resistance": 1},
            {"type": "dark", "resistance": 1},
            {"type": "steel", "resistance": 1},
            {"type": "fairy", "resistance": 1}]


def get_fire_type_defenses():
    return [{"type": "normal", "resistance": 1},
            {"type": "fire", "resistance": .5},
            {"type": "water", "resistance": 2},
            {"type": "electric", "resistance": 1},
            {"type": "grass", "resistance": .5},
            {"type": "ice", "resistance": .5},
            {"type": "fighting", "resistance": 1},
            {"type": "poison", "resistance": 1},
            {"type": "ground", "resistance": 2},
            {"type": "flying", "resistance": 1},
            {"type": "psychic", "resistance": 1},
            {"type": "bug", "resistance": .5},
            {"type": "rock", "resistance": 2},
            {"type": "ghost", "resistance": 1},
            {"type": "dragon", "resistance": 1},
            {"type": "dark", "resistance": 1},
            {"type": "steel", "resistance": .5},
            {"type": "fairy", "resistance": .5}]


def get_water_type_defenses():
    return [{"type": "normal", "resistance": 1},
            {"type": "fire", "resistance": .5},
            {"type": "water", "resistance": .5},
            {"type": "electric", "resistance": 2},
            {"type": "grass", "resistance": 2},
            {"type": "ice", "resistance": .5},
            {"type": "fighting", "resistance": 1},
            {"type": "poison", "resistance": 1},
            {"type": "ground", "resistance": 1},
            {"type": "flying", "resistance": 1},
            {"type": "psychic", "resistance": 1},
            {"type": "bug", "resistance": 1},
            {"type": "rock", "resistance": 1},
            {"type": "ghost", "resistance": 1},
            {"type": "dragon", "resistance": 1},
            {"type": "dark", "resistance": 1},
            {"type": "steel", "resistance": .5},
            {"type": "fairy", "resistance": 1}]


def get_electric_type_defenses():
    return [{"type": "normal", "resistance": 1},
            {"type": "fire", "resistance": 1},
            {"type": "water", "resistance": 1},
            {"type": "electric", "resistance": .5},
            {"type": "grass", "resistance": 1},
            {"type": "ice", "resistance": 1},
            {"type": "fighting", "resistance": 1},
            {"type": "poison", "resistance": 1},
            {"type": "ground", "resistance": 2},
            {"type": "flying", "resistance": .5},
            {"type": "psychic", "resistance": 1},
            {"type": "bug", "resistance": 1},
            {"type": "rock", "resistance": 1},
            {"type": "ghost", "resistance": 1},
            {"type": "dragon", "resistance": 1},
            {"type": "dark", "resistance": 1},
            {"type": "steel", "resistance": .5},
            {"type": "fairy", "resistance": 1}]


def get_grass_type_defenses():
    return [{"type": "normal", "resistance": 1},
            {"type": "fire", "resistance": 2},
            {"type": "water", "resistance": .5},
            {"type": "electric", "resistance": .5},
            {"type": "grass", "resistance": .5},
            {"type": "ice", "resistance": 2},
            {"type": "fighting", "resistance": 1},
            {"type": "poison", "resistance": 2},
            {"type": "ground", "resistance": .5},
            {"type": "flying", "resistance": 2},
            {"type": "psychic", "resistance": 1},
            {"type": "bug", "resistance": 2},
            {"type": "rock", "resistance": 1},
            {"type": "ghost", "resistance": 1},
            {"type": "dragon", "resistance": 1},
            {"type": "dark", "resistance": 1},
            {"type": "steel", "resistance": 1},
            {"type": "fairy", "resistance": 1}]


def get_ice_type_defenses():
    return [{"type": "normal", "resistance": 1},
            {"type": "fire", "resistance": 2},
            {"type": "water", "resistance": 1},
            {"type": "electric", "resistance": 1},
            {"type": "grass", "resistance": 1},
            {"type": "ice", "resistance": .5},
            {"type": "fighting", "resistance": 2},
            {"type": "poison", "resistance": 1},
            {"type": "ground", "resistance": 1},
            {"type": "flying", "resistance": 1},
            {"type": "psychic", "resistance": 1},
            {"type": "bug", "resistance": 1},
            {"type": "rock", "resistance": 2},
            {"type": "ghost", "resistance": 1},
            {"type": "dragon", "resistance": 1},
            {"type": "dark", "resistance": 1},
            {"type": "steel", "resistance": 2},
            {"type": "fairy", "resistance": 1}]


def get_fighting_type_defenses():
    return [{"type": "normal", "resistance": 1},
            {"type": "fire", "resistance": 1},
            {"type": "water", "resistance": 1},
            {"type": "electric", "resistance": 1},
            {"type": "grass", "resistance": 1},
            {"type": "ice", "resistance": 1},
            {"type": "fighting", "resistance": 1},
            {"type": "poison", "resistance": 1},
            {"type": "ground", "resistance": 1},
            {"type": "flying", "resistance": 2},
            {"type": "psychic", "resistance": 2},
            {"type": "bug", "resistance": .5},
            {"type": "rock", "resistance": .5},
            {"type": "ghost", "resistance": 1},
            {"type": "dragon", "resistance": 1},
            {"type": "dark", "resistance": .5},
            {"type": "steel", "resistance": 1},
            {"type": "fairy", "resistance": 2}]


def get_poison_type_defenses():
    return [{"type": "normal", "resistance": 1},
            {"type": "fire", "resistance": 1},
            {"type": "water", "resistance": 1},
            {"type": "electric", "resistance": 1},
            {"type": "grass", "resistance": .5},
            {"type": "ice", "resistance": 1},
            {"type": "fighting", "resistance": .5},
            {"type": "poison", "resistance": .5},
            {"type": "ground", "resistance": 2},
            {"type": "flying", "resistance": 1},
            {"type": "psychic", "resistance": 2},
            {"type": "bug", "resistance": .5},
            {"type": "rock", "resistance": 1},
            {"type": "ghost", "resistance": 1},
            {"type": "dragon", "resistance": 1},
            {"type": "dark", "resistance": 1},
            {"type": "steel", "resistance": 1},
            {"type": "fairy", "resistance": .5}]


def get_ground_type_defenses():
    return [{"type": "normal", "resistance": 1},
            {"type": "fire", "resistance": 1},
            {"type": "water", "resistance": 2},
            {"type": "electric", "resistance": 0},
            {"type": "grass", "resistance": 2},
            {"type": "ice", "resistance": 2},
            {"type": "fighting", "resistance": 1},
            {"type": "poison", "resistance": .5},
            {"type": "ground", "resistance": 1},
            {"type": "flying", "resistance": 1},
            {"type": "psychic", "resistance": 1},
            {"type": "bug", "resistance": 1},
            {"type": "rock", "resistance": .5},
            {"type": "ghost", "resistance": 1},
            {"type": "dragon", "resistance": 1},
            {"type": "dark", "resistance": 1},
            {"type": "steel", "resistance": 1},
            {"type": "fairy", "resistance": 1}]


def get_flying_type_defenses():
    return [{"type": "normal", "resistance": 1},
            {"type": "fire", "resistance": 1},
            {"type": "water", "resistance": 1},
            {"type": "electric", "resistance": 2},
            {"type": "grass", "resistance": .5},
            {"type": "ice", "resistance": 2},
            {"type": "fighting", "resistance": .5},
            {"type": "poison", "resistance": 1},
            {"type": "ground", "resistance": 0},
            {"type": "flying", "resistance": 1},
            {"type": "psychic", "resistance": 1},
            {"type": "bug", "resistance": .5},
            {"type": "rock", "resistance": 2},
            {"type": "ghost", "resistance": 1},
            {"type": "dragon", "resistance": 1},
            {"type": "dark", "resistance": 1},
            {"type": "steel", "resistance": 1},
            {"type": "fairy", "resistance": 1}]


def get_psychic_type_defenses():
    return [{"type": "normal", "resistance": 1},
            {"type": "fire", "resistance": 1},
            {"type": "water", "resistance": 1},
            {"type": "electric", "resistance": 1},
            {"type": "grass", "resistance": 1},
            {"type": "ice", "resistance": 1},
            {"type": "fighting", "resistance": .5},
            {"type": "poison", "resistance": 1},
            {"type": "ground", "resistance": 1},
            {"type": "flying", "resistance": 1},
            {"type": "psychic", "resistance": .5},
            {"type": "bug", "resistance": 2},
            {"type": "rock", "resistance": 1},
            {"type": "ghost", "resistance": 2},
            {"type": "dragon", "resistance": 1},
            {"type": "dark", "resistance": 2},
            {"type": "steel", "resistance": 1},
            {"type": "fairy", "resistance": 1}]


def get_bug_type_defenses():
    return [{"type": "normal", "resistance": 1},
            {"type": "fire", "resistance": 2},
            {"type": "water", "resistance": 1},
            {"type": "electric", "resistance": 1},
            {"type": "grass", "resistance": .5},
            {"type": "ice", "resistance": 1},
            {"type": "fighting", "resistance": .5},
            {"type": "poison", "resistance": 1},
            {"type": "ground", "resistance": .5},
            {"type": "flying", "resistance": 2},
            {"type": "psychic", "resistance": 1},
            {"type": "bug", "resistance": 1},
            {"type": "rock", "resistance": 2},
            {"type": "ghost", "resistance": 1},
            {"type": "dragon", "resistance": 1},
            {"type": "dark", "resistance": 1},
            {"type": "steel", "resistance": 1},
            {"type": "fairy", "resistance": 1}]


def get_rock_type_defenses():
    return [{"type": "normal", "resistance": .5},
            {"type": "fire", "resistance": .5},
            {"type": "water", "resistance": 2},
            {"type": "electric", "resistance": 1},
            {"type": "grass", "resistance": 2},
            {"type": "ice", "resistance": 1},
            {"type": "fighting", "resistance": 2},
            {"type": "poison", "resistance": .5},
            {"type": "ground", "resistance": 2},
            {"type": "flying", "resistance": .5},
            {"type": "psychic", "resistance": 1},
            {"type": "bug", "resistance": 1},
            {"type": "rock", "resistance": 1},
            {"type": "ghost", "resistance": 1},
            {"type": "dragon", "resistance": 1},
            {"type": "dark", "resistance": 1},
            {"type": "steel", "resistance": 2},
            {"type": "fairy", "resistance": 1}]


def get_ghost_type_defenses():
    return [{"type": "normal", "resistance": 0},
            {"type": "fire", "resistance": 1},
            {"type": "water", "resistance": 1},
            {"type": "electric", "resistance": 1},
            {"type": "grass", "resistance": 1},
            {"type": "ice", "resistance": 1},
            {"type": "fighting", "resistance": 0},
            {"type": "poison", "resistance": .5},
            {"type": "ground", "resistance": 1},
            {"type": "flying", "resistance": 1},
            {"type": "psychic", "resistance": 1},
            {"type": "bug", "resistance": .5},
            {"type": "rock", "resistance": 1},
            {"type": "ghost", "resistance": 2},
            {"type": "dragon", "resistance": 1},
            {"type": "dark", "resistance": 2},
            {"type": "steel", "resistance": 1},
            {"type": "fairy", "resistance": 1}]


def get_dragon_type_defenses():
    return [{"type": "normal", "resistance": 1},
            {"type": "fire", "resistance": .5},
            {"type": "water", "resistance": .5},
            {"type": "electric", "resistance": .5},
            {"type": "grass", "resistance": .5},
            {"type": "ice", "resistance": 2},
            {"type": "fighting", "resistance": 1},
            {"type": "poison", "resistance": 1},
            {"type": "ground", "resistance": 1},
            {"type": "flying", "resistance": 1},
            {"type": "psychic", "resistance": 1},
            {"type": "bug", "resistance": 1},
            {"type": "rock", "resistance": 1},
            {"type": "ghost", "resistance": 1},
            {"type": "dragon", "resistance": 2},
            {"type": "dark", "resistance": 1},
            {"type": "steel", "resistance": 1},
            {"type": "fairy", "resistance": 2}]


def get_dark_type_defenses():
    return [{"type": "normal", "resistance": 1},
            {"type": "fire", "resistance": 1},
            {"type": "water", "resistance": 1},
            {"type": "electric", "resistance": 1},
            {"type": "grass", "resistance": 1},
            {"type": "ice", "resistance": 1},
            {"type": "fighting", "resistance": 2},
            {"type": "poison", "resistance": 1},
            {"type": "ground", "resistance": 1},
            {"type": "flying", "resistance": 1},
            {"type": "psychic", "resistance": 0},
            {"type": "bug", "resistance": 2},
            {"type": "rock", "resistance": 1},
            {"type": "ghost", "resistance": .5},
            {"type": "dragon", "resistance": 1},
            {"type": "dark", "resistance": .5},
            {"type": "steel", "resistance": 1},
            {"type": "fairy", "resistance": 2}]


def get_steel_type_defenses():
    return [{"type": "normal", "resistance": .5},
            {"type": "fire", "resistance": 2},
            {"type": "water", "resistance": 1},
            {"type": "electric", "resistance": 1},
            {"type": "grass", "resistance": .5},
            {"type": "ice", "resistance": .5},
            {"type": "fighting", "resistance": 2},
            {"type": "poison", "resistance": 0},
            {"type": "ground", "resistance": 2},
            {"type": "flying", "resistance": .5},
            {"type": "psychic", "resistance": .5},
            {"type": "bug", "resistance": .5},
            {"type": "rock", "resistance": .5},
            {"type": "ghost", "resistance": 1},
            {"type": "dragon", "resistance": .5},
            {"type": "dark", "resistance": 1},
            {"type": "steel", "resistance": .5},
            {"type": "fairy", "resistance": .5}]


def get_fairy_type_defenses():
    return [{"type": "normal", "resistance": 1},
            {"type": "fire", "resistance": 1},
            {"type": "water", "resistance": 1},
            {"type": "electric", "resistance": 1},
            {"type": "grass", "resistance": 1},
            {"type": "ice", "resistance": 1},
            {"type": "fighting", "resistance": .5},
            {"type": "poison", "resistance": 2},
            {"type": "ground", "resistance": 1},
            {"type": "flying", "resistance": 1},
            {"type": "psychic", "resistance": 1},
            {"type": "bug", "resistance": .5},
            {"type": "rock", "resistance": 1},
            {"type": "ghost", "resistance": 1},
            {"type": "dragon", "resistance": 0},
            {"type": "dark", "resistance": .5},
            {"type": "steel", "resistance": 2},
            {"type": "fairy", "resistance": 1}]


def get_type_stats_from_name(type_name):
    match type_name:
        case "normal":
            return get_normal_type_defenses()
        case "fire":
            return get_fire_type_defenses()
        case "water":
            return get_water_type_defenses()
        case "electric":
            return get_electric_type_defenses()
        case "grass":
            return get_grass_type_defenses()
        case "ice":
            return get_ice_type_defenses()
        case "fighting":
            return get_fighting_type_defenses()
        case "poison":
            return get_poison_type_defenses()
        case "ground":
            return get_ground_type_defenses()
        case "flying":
            return get_flying_type_defenses()
        case "psychic":
            return get_psychic_type_defenses()
        case "bug":
            return get_bug_type_defenses()
        case "rock":
            return get_rock_type_defenses()
        case "ghost":
            return get_ghost_type_defenses()
        case "dragon":
            return get_dragon_type_defenses()
        case "dark":
            return get_dark_type_defenses()
        case "steel":
            return get_steel_type_defenses()
        case "fairy":
            return get_fairy_type_defenses()
