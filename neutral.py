from units_class import Unit
import pygame
from func_load_image import load_image


def create_dict_neutral(link):
    c = link.split('/')
    c = '/'.join(c[:-1]) + '/neutral' + c[-1].split('.')[0][-1] + '.txt'
    neutrals_coords = {}
    r = open(f'{c}', mode="rt").readlines()
    for i in r:
        key, arg = i.rstrip().split('-')
        key = tuple(int(i) for i in key.split(':'))
        arg = list([i[0], int(i[1:])] for i in arg.split(':'))
        for _ in range(6 - len(arg)):
            arg.append(False)
        neutrals_coords[key] = arg
    return neutrals_coords


def neutral_in_arms(netr):
    return ([Unit(i[0]), i[1]] if i else i for i in netr)


def battle_scoring(hero_units, additional_h, neutrals, additional_e=(0, 0, 0, 0)):
    hero_units, neutrals = list(hero_units), list(neutrals)
    if sum(i[1] * i[0].scroll(*additional_h) for i in hero_units if type(i) != bool) >= sum(
            i[1] * int(i[0].scroll(*additional_e)) for i in neutrals if type(i) != bool):
        casualties = int(sum(i[1] * i[0].scroll(*additional_e) for i in neutrals if type(i) != bool))
        survivors = []
        for i in range(len(hero_units)):
            if type(hero_units[i]) != bool:
                unit = hero_units[i][1] * hero_units[i][0].scroll(*additional_h)
                if unit <= casualties:
                    casualties -= unit
                else:
                    survivors.append([hero_units[i][0], int(((unit - casualties) // int(hero_units[i][0].scroll(*additional_h))))])
                    survivors += hero_units[i + 1:]

        survivors = tuple(survivors) + tuple(False for _ in range(6 - len(survivors)))
        return True, list(survivors), 0
    else:
        return False,


def battle_enemis_scoring(hero_units, additional_h, neutrals):
    return battle_scoring(hero_units, additional_h, neutral_in_arms(neutrals))


def battle_enemis_hero_scoring(hero_units, additional_h, enemi_hero_units, additional_e):
    return battle_scoring(hero_units, additional_h, enemi_hero_units, additional_e=additional_e)


def draw_preparation_window(army1, army2):
    army2 = list(army2)
    d = {'peasant': load_image('krestianin_ikonka.png'),
         'penny': load_image('kopeishik_ikonka.png'),
         'swordman': load_image('mechnik_ikonka.png'),
         'knight': load_image('knight_ikonka.png'),
         'archer': load_image('luchnick_ikonka.png'),
         'crossbowman': load_image('arbaletchik_ikonka.png'),
         'cleric': load_image('clerick_ikonka.png'),
         'abbot': load_image('abbot_ikonka.png'),
         'horseman': load_image('vsadnik_ikonka.png'),
         'master of light and might': load_image('angel_ikonka.png')}
    board_img = load_image('board.png', colorkey=-1)
    rect = board_img.get_rect()
    for i in range(5, 86, 72):
        board_img.blit(pygame.transform.scale(load_image('mesto_avatara.png', colorkey=-1),
                                              (int(rect[2] * 0.2), int(rect[3] * 0.2))),
                       (int(rect[2] * i // 100), int(rect[3] * 0.05)))
        ava = load_image('hero_avatar_1.png', colorkey=-1) if i < 10 else load_image('hero_avatar_2.png', colorkey=-1)
        board_img.blit(pygame.transform.scale(ava, (int(rect[2] * 0.15), int(rect[3] * 0.15))),
                       (int(rect[2] * (i + 3) // 100), int(rect[3] * 0.05)))
    m_arm = load_image('12620557_4Z_2101.w017.n001.350A.p30.350.png', colorkey=-1)

    for y, i in zip(range(25, 56, 30), range(1, 3)):
        for x, ii in zip(range(5, 36, 15), range(1, 4)):
            board_img.blit(
                pygame.transform.scale(m_arm,
                                       (int(rect[2] * 0.15), int(rect[2] * 0.15))),
                (int(rect[2] * x // 100), int(rect[3] * y // 100)))
            if army1[i * ii - 1]:
                board_img.blit(
                    pygame.transform.scale(d[army1[i * ii - 1][0].name],
                                           (int(rect[2] * 0.15 * 0.95), int(rect[2] * 0.15 * 0.95))),
                    (int(rect[2] * (x / 100)), int(rect[3] * (y / 100))))
                font = pygame.font.Font(None, 500)
                text_surface = font.render(str(army1[i * ii - 1][1]), True, (218, 165, 32))
                board_img.blit(text_surface, (int(rect[2] * (x + 5) / 100), int(rect[3] * (y + 22) / 100)))
        for x, ii in zip(range(50, 81, 15), range(1, 4)):
            board_img.blit(
                pygame.transform.scale(m_arm,
                                       (int(rect[2] * 0.15), int(rect[2] * 0.15))),
                (int(rect[2] * x // 100), int(rect[3] * y // 100)))
            if army2[i * ii - 1]:
                board_img.blit(
                    pygame.transform.scale(d[army2[i * ii - 1][0].name],
                                           (int(rect[2] * 0.15 * 0.95), int(rect[2] * 0.15 * 0.95))),
                    (int(rect[2] * (x / 100)), int(rect[3] * (y / 100))))
                font = pygame.font.Font(None, 500)
                text_surface = font.render(str(army2[i * ii - 1][1]), True, (218, 165, 32))
                board_img.blit(text_surface, (int(rect[2] * (x + 5) / 100), int(rect[3] * (y + 22) / 100)))
    return board_img
