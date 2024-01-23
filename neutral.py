from units_class import Unit


def create_dict_neutral(link):
    c = link.split('/')
    c = '/'.join(c[:-1]) + 'neutral' + c[-1].split('.')[0][-1] + '.txt'
    neutrals_coords = {}
    r = open(f'{c}', mode="r").readlines()
    for i in r:
        key, arg = i.rstrip().split('-')
        key = tuple(int(i) for i in key.split(':'))
        arg = tuple([i[0], int(i[1:])] for i in arg.split(':'))
        neutrals_coords[key] = arg
    return neutrals_coords


def neutral_in_arms(netr):
    return ([Unit(i[0]), i[1:]] for i in netr)


def battle_scoring(hero_units, additional_h, neutrals, additional_e=(0, 0, 0, 0)):
    if sum(i[1] * i[0].scroll(*additional_h) for i in hero_units) >= sum(
            i[1] * i[0].scroll(*additional_e) for i in neutrals):
        casualties = sum(i[1] * i[0].scroll(*additional_e) for i in neutrals)
        survivors = []
        for i in hero_units:
            unit = i[1] * i[0].scroll(*additional_h)
            if unit <= casualties:
                casualties -= unit
            else:
                survivors.append([i[0], -1 * int(-(
                        (i[1] * i[0].health_points - i[1].point_to_health(*additional_h, casualties)) / i[
                    0].health_points))])
        return True, survivors
    else:
        return False,


def battle_enemis_scoring(hero_units, additional_h, neutrals):
    return battle_scoring(hero_units, additional_h, neutral_in_arms(neutrals))


def battle_enemi_hero_scoring(hero_units, additional_h, enemi_hero_units, additional_e):
    return battle_scoring(hero_units, additional_h, enemi_hero_units, additional_e=additional_e)

