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


def draw_preparation_window(army1, army2):
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
    for i in range(5, 96, 90):
        board_img.blit(pygame.transform.scale(load_image('mesto_avatara.png', colorkey=-1),
                                              (int(rect[0] * 0.1), int(rect[1] * 0.1))),
                       (int(rect[0] * i // 100), int(rect[1] * 0.05)))
        ava = load_image('hero_avatar_1.png', colorkey=-1) if i < 10 else load_image('hero_avatar_2.png', colorkey=-1)
        board_img.blit(pygame.transform.scale(ava, (int(rect[0] * 0.1 * 0.6), int(rect[1] * 0.1 * 0.7))),
                       (int(rect[0] * i // 100 * 1.2), int(rect[1] * 0.05 * 0.15)))
    m_arm = load_image('12620557_4Z_2101.w017.n001.350A.p30.350.png', colorkey=-1)

    for y, i in zip(range(15, 26, 10), range(1, 3)):
        for x, ii in zip(range(15, 46, 15), range(1, 4)):
            board_img.blit(
                pygame.transform.scale(m_arm,
                                       (int(rect[0] * 0.1), int(rect[1] * 0.1))),
                (int(rect[0] * x // 100), int(rect[1] * y // 100)))
            board_img.blit(
                pygame.transform.scale(d[army1[i * ii][0].name], (int(rect[0] * 0.1 * 0.6), int(rect[1] * 0.1 * 0.7))),
                (int(rect[0] * x // 100 * 1.2), int(rect[1] * y // 100 * 0.15)))
            font = pygame.font.Font(None, int(rect[0] * 0.1 * 0.1))
            text_surface = font.render(str(army1[i * ii][1]), True, (255, 255, 255))
            board_img.blit(text_surface, (int(rect[0] * x * 1.1 // 100), int(rect[1] * y * 1.1 // 100)))
        for x, ii in zip(range(55, 101, 15), range(1, 4)):
            board_img.blit(
                pygame.transform.scale(m_arm,
                                       (int(rect[0] * 0.1), int(rect[1] * 0.1))),
                (int(rect[0] * x // 100), int(rect[1] * y // 100)))
            board_img.blit(
                pygame.transform.scale(d[army2[i * ii][0].name], (int(rect[0] * 0.1 * 0.6), int(rect[1] * 0.1 * 0.7))),
                (int(rect[0] * x // 100 * 1.2), int(rect[1] * y // 100 * 0.15)))
            font = pygame.font.Font(None, int(rect[0] * 0.1 * 0.1))
            text_surface = font.render(str(army2[i * ii][1]), True, (255, 255, 255))
            board_img.blit(text_surface, (int(rect[0] * x * 1.1 // 100), int(rect[1] * y * 1.1 // 100)))
    return board_img
