from menu_start import BasicMenu
from func_load_image import load_image
from buton import ImageButton
from shablon import Hero, AnimatedSprite
from fog_war import create_fog_war, change_fog_war
from on_screen import chunks_on_screen, resources_on_screen
from neutral import create_dict_neutral, draw_preparation_window, neutral_in_arms, battle_enemis_scoring, \
    battle_enemis_hero_scoring
from buildings import Buildings, RedCastle, BlueCastle
import pygame  # импорт библиотеки PyGame
import random
import sqlite3
import os

pygame.init()  # инициализируем PyGame

WIDTH = 1920  # ширина экрана
HEIGHT = 1080  # высота экрана

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создаем поверхность экрана

current_scene = lambda x: 1
fon_download = 'fon_download.png'
image = "zamok_gorod_fentezi_174584_1920x1080.jpg"

link_sprites_hero1 = 'hero1_standing.png'
link_sprites_hero2 = 'hero2_standing.png'

scroll = load_image('pixel-scroll-ribbon-ancient-manuscript-parchment-banner_158677-1477.png', -1)

img_objects_map = {'A': load_image('hero1.png', colorkey=-1),
                   'B': load_image('hero2.png', colorkey=-1),
                   '#': load_image('kust.png'),
                   '-': load_image('1626746394_9-kartinkin-com-p-pikselnaya-tekstura-travi-krasivo-11.jpg'),
                   '*': load_image('abstract-blue-painting-acrylic-texture-with-marble-pattern.jpg', colorkey=-1),
                   '@': load_image('castle1.png', colorkey=-1),
                   '$': load_image('castle2.png', colorkey=-1),
                   'G': load_image('1677316897_foni-club-p-sunduk-piksel-art-1.png', colorkey=-1),
                   'W': load_image('—Pngtree—wood log lumber pile cartoon_6955308.png', colorkey=-1),
                   'R': load_image('photo1705405793.png', colorkey=-1),
                   'M': load_image('kristal.png', colorkey=-1),
                   'O': load_image('image0000.png', colorkey=-1),
                   'K': load_image('b94adf7c5d21d13a83be3878336d0378.png', colorkey=-1),
                   'I': load_image('klipartz.com.png', colorkey=-1),
                   'F': load_image('gadalka.png', colorkey=-1),
                   '1': load_image('as.png', colorkey=-1),
                   '2': load_image('34174417_2210_w032_n002_608b_p15_608.png', colorkey=-1),
                   '3': load_image('molot.png', colorkey=-1),
                   '4': load_image('msg1331310743-41499.png', colorkey=-1),
                   '5': load_image('70015845_JEMA GER 1640-02.png', colorkey=-1)
                   }

sprites_enemies = {}


def switch_scene(scene):
    global current_scene
    current_scene = scene


def setting_screen():
    menu = BasicMenu()
    menu.append_option('Играть', lambda: switch_scene(game_world_draw))
    menu.append_option('Выбрать размер', lambda: quit)
    menu.append_option('Вернуться', lambda: switch_scene(basic_menu_draw))
    running = True
    screen.blit(load_image(image), (0, 0))
    menu.draw(screen, 800, 400, 75)
    while running:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                running = False
                menu.click(e.pos)
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    switch_scene(None)
                elif e.key == pygame.K_w:
                    menu.switch(-1)
                elif e.key == pygame.K_s:
                    menu.switch(1)
                elif e.key == pygame.K_SPACE:
                    menu.select()
                    running = False
        screen.blit(load_image(image), (0, 0))
        menu.draw(screen, 800, 400, 75)
        pygame.display.flip()


def basic_menu_draw(*args):
    global screen
    size = 1920, 1080
    screen = pygame.display.set_mode(size)
    menu = BasicMenu()
    menu.append_option('      1 VS 1      ', lambda: switch_scene(menu_draw))
    menu.append_option('Размер экрана', lambda: switch_scene(setting_screen))
    menu.append_option('      Выйти      ', quit)
    running = True
    screen.blit(load_image(image), (0, 0))
    menu.draw(screen, 800, 400, 75)
    while running:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                menu.click(e.pos)
                running = False
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    switch_scene(None)
                elif e.key == pygame.K_w:
                    menu.switch(-1)
                elif e.key == pygame.K_s:
                    menu.switch(1)
                elif e.key == pygame.K_SPACE:
                    menu.select()
                    running = False
        screen.blit(load_image(image), (0, 0))
        menu.draw(screen, 800, 400, 75)
        pygame.display.flip()


def menu_draw(*args):
    size = 1920, 1080
    global screen
    screen = pygame.display.set_mode(size)
    menu = BasicMenu()
    menu.append_option('Играть', lambda: switch_scene(game_world_draw))
    menu.append_option('Выбрать карту', lambda: switch_scene(select_map_1()))
    menu.append_option('Вернуться', lambda: switch_scene(basic_menu_draw))
    running = True
    screen.blit(load_image(image), (0, 0))
    menu.draw(screen, 800, 400, 75)
    while running:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                running = False
                menu.click(e.pos)
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    switch_scene(None)
                elif e.key == pygame.K_w:
                    menu.switch(-1)
                elif e.key == pygame.K_s:
                    menu.switch(1)
                elif e.key == pygame.K_SPACE:
                    menu.select()
                    running = False
        screen.blit(load_image(image), (0, 0))
        menu.draw(screen, 800, 400, 75)
        pygame.display.flip()


def select_map_1():
    size = 1920, 1080
    global screen
    global data_game
    screen = pygame.display.set_mode(size)
    menu = BasicMenu()

    db = "GameDB.db3"
    db = os.path.join('data/db', db)
    con = sqlite3.connect(db)
    cur = con.cursor()
    result = cur.execute("""SELECT name, description, link FROM maps WHERE id = 1""").fetchall()

    menu.append_option(f'{result[0][0]}', lambda: switch_scene(select_map_1))
    menu.append_option('...', lambda: switch_scene(select_map_2))
    menu.append_option('Вернуться', lambda: switch_scene(menu_draw))

    description_text = result[0][1].split('\\n')
    selected_map = result[0][2]
    description_1 = pygame.font.SysFont('arial', 44).render(description_text[0], True, (255, 255, 255))
    description_2 = pygame.font.SysFont('arial', 44).render(description_text[1], True, (255, 255, 255))
    running = True
    screen.blit(load_image(image), (0, 0))
    menu.draw(screen, 400, 400, 75)
    buttons = [ImageButton(920, 625, 1000, 350, '', 'scroll.png',
                           hover_image_path='scroll.png'),
               ImageButton(375, 800, 300, 200, 'ВЫБРАТЬ',
                           '—Pngtree—buttons games button illustration_5544907.png',
                           hover_image_path='—Pngtree—buttons games button illustration_5544907_2.png')
               ]
    while running:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                running = False
                menu.click(e.pos)
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    switch_scene(None)
                elif e.key == pygame.K_w:
                    menu.switch(-1)
                elif e.key == pygame.K_s:
                    menu.switch(1)
                elif e.key == pygame.K_SPACE:
                    menu.select()
                    running = False
            for button in buttons:
                button.handle_event(e)
            if e.type == pygame.USEREVENT:
                if e.button == buttons[1]:
                    data_game = f'data/maps/{selected_map}'
        screen.blit(load_image(image), (0, 0))
        for button in buttons:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(screen)
        screen.blit(description_1, (1100, 700))
        screen.blit(description_2, (1100, 800))
        menu.draw(screen, 400, 400, 75)
        pygame.display.flip()


def select_map_2():
    size = 1920, 1080
    global screen
    global data_game

    db = "GameDB.db3"
    db = os.path.join('data/db', db)
    con = sqlite3.connect(db)
    cur = con.cursor()
    result = cur.execute("""SELECT name, description, link FROM maps WHERE id = 2""").fetchall()

    screen = pygame.display.set_mode(size)
    menu = BasicMenu()
    menu.append_option(f'{result[0][0]}', lambda: switch_scene(select_map_1))
    menu.append_option(f'{result[0][1]}', lambda: switch_scene(select_map_2))
    menu.append_option('Вернуться', lambda: switch_scene(menu_draw))

    description_text = result[1][1].split('\\n')
    selected_map = result[1][2]
    description_1 = pygame.font.SysFont('arial', 44).render(description_text[0], True, (255, 255, 255))
    description_2 = pygame.font.SysFont('arial', 44).render(description_text[1], True, (255, 255, 255))
    running = True
    screen.blit(load_image(image), (0, 0))
    menu.draw(screen, 400, 400, 75)
    buttons = [ImageButton(920, 625, 1000, 350, '', 'scroll.png',
                           hover_image_path='scroll.png'),
               ImageButton(375, 800, 300, 200, 'ВЫБРАТЬ',
                           '—Pngtree—buttons games button illustration_5544907.png',
                           hover_image_path='—Pngtree—buttons games button illustration_5544907_2.png')
               ]
    while running:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                running = False
                menu.click(e.pos)
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    switch_scene(None)
                elif e.key == pygame.K_w:
                    menu.switch(-1)
                elif e.key == pygame.K_s:
                    menu.switch(1)
                elif e.key == pygame.K_SPACE:
                    menu.select()
                    running = False
            for button in buttons:
                button.handle_event(e)
            if e.type == pygame.USEREVENT:
                if e.button == buttons[1]:
                    data_game = f'data/maps/{selected_map}'
        screen.blit(load_image(image), (0, 0))
        for button in buttons:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(screen)
        screen.blit(description_1, (1100, 700))
        screen.blit(description_2, (1100, 800))
        menu.draw(screen, 400, 400, 75)
        pygame.display.flip()


def game_world_draw(*args):
    print(args)
    args = args[0]
    print(args[0])
    flag_data = True if len(args) > 1 else False
    link_map = args[0]

    size = [1920, 1080]
    res = [480, 260]

    if flag_data:
        print(args[1])
    cam_x, cam_y = (0, 0) if not flag_data else args[1]
    global screen
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    window = pygame.transform.scale(screen, res)
    surface = pygame.display.get_surface()
    size = [surface.get_width(), surface.get_height()]

    clock = pygame.time.Clock()

    chunk_size = 8 if not flag_data else args[2]
    tile_size = 24 if not flag_data else args[3]

    neutral_dict = create_dict_neutral(link_map)

    sprites_enemies_i = {'k': 0, 'K': 1, 's': 2, 'S': 3, 'a': 4, 'A': 5, 'c': 6, 'C': 7, 'H': 8, 'M': 9}

    r = open(f'{link_map}', mode="r").readlines()
    map = [i.rstrip() + '#' * (chunk_size - len(r[0][:-3]) % chunk_size) for i in r]
    map = map + ['#' * len(map[0])] * (chunk_size - len(map) % chunk_size)
    map = [list(i) for i in map] if not flag_data else args[4]
    one_player_fog_war = create_fog_war(map, 'A') if not flag_data else args[5]
    two_player_fog_war = create_fog_war(map, 'B') if not flag_data else args[6]

    world_size_chunk_x = len(map[0]) // chunk_size if not flag_data else args[7]
    world_size_chunk_y = len(map) // chunk_size if not flag_data else args[8]

    hero1_animated = AnimatedSprite(load_image(link_sprites_hero1, colorkey=-1), 3, 1, tile_size, tile_size)
    hero2_animated = AnimatedSprite(load_image(link_sprites_hero2, colorkey=-1), 3, 1, tile_size, tile_size)

    sprites_enemies = [AnimatedSprite(load_image('Peasant.png'), 4, 1, tile_size, tile_size),
                       AnimatedSprite(load_image('Peasant1.png', colorkey=-1), 13, 1, tile_size, tile_size),
                       AnimatedSprite(load_image('Swordmaster.png', colorkey=-1), 3, 1, tile_size, tile_size),
                       AnimatedSprite(load_image('Swordmaster1.png', colorkey=-1), 3, 1, tile_size, tile_size),
                       AnimatedSprite(load_image('Archer.png', colorkey=-1), 9, 1, tile_size, tile_size),
                       AnimatedSprite(load_image('Archer1.png', colorkey=-1), 13, 1, tile_size, tile_size),
                       AnimatedSprite(load_image('Cleric.png', colorkey=-1), 13, 1, tile_size, tile_size),
                       AnimatedSprite(load_image('Cleric1.png', colorkey=-1), 13, 1, tile_size, tile_size),
                       AnimatedSprite(load_image('Cavalier1.png', colorkey=-1), 28, 1, tile_size, tile_size),
                       AnimatedSprite(load_image('Emperor.png', colorkey=-1), 5, 1, tile_size, tile_size)]

    class Chunk:
        fog_tiel = pygame.transform.scale(
            load_image('900144_3876.jpg'),
            (tile_size, tile_size))
        trava = pygame.transform.scale(
            load_image('1626746394_9-kartinkin-com-p-pikselnaya-tekstura-travi-krasivo-11.jpg'),
            (tile_size, tile_size))

        def __init__(self, coord_tiel, x, y):
            self.n_tiel_x, self.n_tiel_y = coord_tiel
            self.x, self.y = x, y

        def render(self, fog):
            pas = (False, (0, 0))
            for y in range(chunk_size):
                for x in range(chunk_size):
                    fog_flag = fog[self.n_tiel_y + y][self.n_tiel_x + x - 1]
                    screen.blit(Chunk.trava if not fog_flag else Chunk.fog_tiel,
                                (self.x + x * tile_size - cam_x, self.y + y * tile_size - cam_y))

                    if pas[0]:
                        key = map[self.n_tiel_y + pas[1][0]][self.n_tiel_x + pas[1][1] - 1]
                        texture = pygame.transform.scale(
                            img_objects_map[key],
                            (tile_size * 3, tile_size * 3))
                        screen.blit(texture,
                                    (self.x + (pas[1][1] - 1) * tile_size - cam_x,
                                     self.y + (pas[1][0] - 2) * tile_size - cam_y))
                        pas = (False, (0, 0))
                        continue
                    if not fog_flag:
                        key = map[self.n_tiel_y + y][self.n_tiel_x + x - 1]
                        if key in 'AB':
                            if key == 'A':
                                texture = pygame.transform.scale(hero1_animated.image, (tile_size, tile_size))
                                screen.blit(texture, (self.x + x * tile_size - cam_x, self.y + y * tile_size - cam_y))
                            else:
                                texture = pygame.transform.scale(hero2_animated.image, (tile_size, tile_size))
                                screen.blit(texture, (self.x + x * tile_size - cam_x, self.y + y * tile_size - cam_y))
                        elif key in 'OKIF@$':
                            pas = (True, (y, x))
                        elif key == '/':
                            pass
                        elif key == 'V':
                            v = neutral_dict[(self.n_tiel_y + y, self.n_tiel_x + x - 1)]
                            texture = pygame.transform.scale(sprites_enemies[sprites_enemies_i[v[0][0]]].image,
                                                             (tile_size, tile_size))
                            screen.blit(texture, (self.x + x * tile_size - cam_x, self.y + y * tile_size - cam_y))
                        else:
                            texture = pygame.transform.scale(
                                img_objects_map[key],
                                (tile_size, tile_size))
                            screen.blit(texture, (self.x + x * tile_size - cam_x, self.y + y * tile_size - cam_y))

    running = True
    chunks = []
    for y in range(world_size_chunk_y):
        for x in range(world_size_chunk_x):
            chunks.append(
                Chunk((x * chunk_size, y * chunk_size), x * chunk_size * tile_size, y * chunk_size * tile_size))

    buttons = [ImageButton(int(res[0] * 0.88), int(res[1] * 0.85), int(res[0] * 0.1), int(res[1] * 0.13), '',
                           'photo1705490612.png', hover_image_path='photo1705490612_2.png',
                           sound_path='data/musik/razrezayuschiy-udar-mechom.mp3'),
               ImageButton(int(res[0] * 0.03), int(res[1] * 0.83), int(res[0] * 0.1), int(res[1] * 0.15), '',
                           'pngwing.com.png', hover_image_path='pngwing_2.com.png',
                           sound_path='data/musik/orkestr-tojdestvennyiy-akkord-s-trubami.mp3'),
               ImageButton(int(res[0] * 0.85), int(res[1] * 0), int(res[0] * 0.15), int(res[1] * 0.1), 'Exit',
                           '—Pngtree—buttons games button illustration_5544907.png',
                           hover_image_path='—Pngtree—buttons games button illustration_5544907_2.png'),
               ImageButton(int(res[0] * 0.78), int(res[1] * 0.85), int(res[0] * 0.1), int(res[1] * 0.13), '',
                           'pixel-castle-for-games-and-web-sites-400-111240444.png',
                           hover_image_path='pixel-castle_2-for-games-and-web-sites-400-111240444.png',
                           sound_path='data/musik/torjestvennyiy-zvuk-fanfar.mp3')
               ]
    buttons_board = [ImageButton(int(res[0] * 0.4), int(res[1] * 0.7), int(res[0] * 0.2), int(res[1] * 0.2), '',
                                 'knight_buying_ikonka.jpg', hover_image_path='knight_buying_ikonka1.jpg',
                                 sound_path='data/musik/zvon-lezviya-dostannogo-mecha-iz-nojen.mp3'),
                     ImageButton(int(res[0] * 0.8), int(res[1] * 0), int(res[0] * 0.2), int(res[1] * 0.15), '',
                                 'krest1.png', hover_image_path='krest2.png')
                     ]

    sum_day = 0 if not flag_data else args[9]
    flag_player = True if not flag_data else args[10]

    players_hero = [Hero('A', 2), Hero('B', 3)] if not flag_data else args[11]  # !!!!! нужно подключить армию
    players_hero[0].find_hero_coords(map)
    players_hero[1].find_hero_coords(map)

    steps_current_hero = (players_hero[0 if flag_player else 1].give_hero_steps()) if not flag_data else args[12]
    current_fog = (one_player_fog_war if flag_player else two_player_fog_war) if not flag_data else args[13]

    sps_resources_img = pygame.transform.scale(
        load_image('pile-of-gold-in-pixel-art-style_475147-1963.jpg', -1),
        (int(res[0] * 0.7) // 10, int(int(res[1] * 0.15) * 0.6))), pygame.transform.scale(
        load_image('n6tp_bfnl_210603.png', -1),
        (int(res[0] * 0.7) // 10,
         int(int(res[1] * 0.15) * 0.6))), pygame.transform.scale(
        load_image('photo1705405793.png', -1),
        (int(res[0] * 0.7) // 10, int(int(res[1] * 0.15) * 0.6))), pygame.transform.scale(
        load_image('kristal.png', -1),
        (int(res[0] * 0.7) // 10, int(int(res[1] * 0.15) * 0.6))), pygame.transform.scale(load_image(
        'pixel-art-illustration-boots-pixelated-boots-autumn-boots-shoes-icon-pixelated-for-the-pixel-art_1038602-215.jpg',
        -1), (int(res[0] * 0.7) // 10, int(int(res[1] * 0.15) * 0.6)))

    preparation_window = 0, load_image('sheaf_spears.jpg'), (0, 0)

    winner = ''

    frame = 0 if not flag_data else args[14]

    def go_hero(map, steps_current_hero, current_fog, cam_y, cam_x, direction_y, direction_x, chr_to_replace=''):
        steps_current_hero -= 1
        if not chr_to_replace:
            map[players_hero[id_hero].y_hero + direction_y][players_hero[id_hero].x_hero + direction_x], \
            map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero] = \
                map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero], \
                map[players_hero[id_hero].y_hero + direction_y][players_hero[id_hero].x_hero + direction_x]
        else:
            map[players_hero[id_hero].y_hero + direction_y][players_hero[id_hero].x_hero + direction_x], \
            map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero] = \
                map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero], chr_to_replace
        players_hero[id_hero].set_hero_coords(players_hero[id_hero].y_hero + direction_y,
                                              players_hero[id_hero].x_hero + direction_x)
        current_fog = change_fog_war(map, current_fog, players_hero[id_hero].chr)
        if not (e.mod == pygame.KMOD_LSHIFT):
            cam_y, cam_x = (i * tile_size - ii // 2 for i, ii in
                            zip(players_hero[id_hero].give_hero_coords(), res[::-1]))
        return map, steps_current_hero, current_fog, cam_y, cam_x

    def visit_the_building(steps_current_hero, direction_y, direction_x, chr, player_hero):
        steps_current_hero -= 1
        coords_build = (player_hero.y_hero + direction_y, player_hero.x_hero + direction_x)
        if coords_build not in player_hero.visited_buildings:
            player_hero.add_visited_building(*coords_build)
            if chr == 'O':
                player_hero.attack += 1
            elif chr == 'K':
                player_hero.protection += 1
            elif chr == 'I':
                player_hero.inspiration += 1
            else:
                player_hero.luck += 1
        return steps_current_hero, player_hero

    def take_the_artifact(map, steps_current_hero, current_fog, cam_y, cam_x, direction_y, direction_x, hero, chr,
                          chr_to_replace=''):
        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero, current_fog, cam_y, cam_x,
                                                                     direction_y, direction_x,
                                                                     chr_to_replace=chr_to_replace)
        hero.add_artefats(chr)
        return map, steps_current_hero, current_fog, cam_y, cam_x, hero

    while running:

        screen.blit(load_image(fon_download), (0, 0))
        if flag_player:
            id_hero = 0
        else:
            id_hero = 1
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    switch_scene(None)
                elif (e.key == pygame.K_UP or e.key == pygame.K_KP8) and steps_current_hero:

                    chr_go = map[players_hero[id_hero].y_hero - 1][players_hero[id_hero].x_hero]
                    if chr_go == '-':
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, -1, 0)
                    elif chr_go == 'G':
                        players_hero[id_hero].gold += random.randrange(1000, 2001, 1000)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, -1, 0,
                                                                                     chr_to_replace='-')
                    elif chr_go == 'W':
                        players_hero[id_hero].wood += random.randrange(1, 4)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, -1, 0,
                                                                                     chr_to_replace='-')
                    elif chr_go == 'R':
                        players_hero[id_hero].rock += random.randrange(1, 4)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, -1, 0,
                                                                                     chr_to_replace='-')
                    elif chr_go == 'M':
                        players_hero[id_hero].cristal += random.randrange(1, 3)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, -1, 0,
                                                                                     chr_to_replace='-')
                    elif any(chr_go == i for i in 'OKIF'):
                        steps_current_hero, players_hero[id_hero] = list(visit_the_building(steps_current_hero, -1, 0,
                                                                                            chr_go,
                                                                                            players_hero[id_hero]))
                    elif any(chr_go == i for i in '12345'):
                        map, steps_current_hero, current_fog, cam_y, cam_x, players_hero[id_hero] = take_the_artifact(
                            map, steps_current_hero, current_fog, cam_y, cam_x, -1, 0, players_hero[id_hero], chr_go,
                            chr_to_replace='-')
                    elif chr_go == 'V':
                        preparation_window = 1, draw_preparation_window(players_hero[id_hero].slots_army,
                                                                        neutral_in_arms(neutral_dict[(
                                                                            players_hero[id_hero].y_hero - 1,
                                                                            players_hero[id_hero].x_hero)])), (-1, 0)
                    elif any(chr_go == i for i in 'AB'):
                        preparation_window = 2, draw_preparation_window(players_hero[id_hero].slots_army,
                                                                        players_hero[::-1][id_hero].slots_army), (-1, 0)
                elif (e.key == pygame.K_DOWN or e.key == pygame.K_KP2) and steps_current_hero:
                    chr_go = map[players_hero[id_hero].y_hero + 1][players_hero[id_hero].x_hero]
                    if chr_go == '-':
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 1,
                                                                                     0)
                    elif chr_go == 'G':
                        players_hero[id_hero].gold += random.randrange(1000, 2001, 1000)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 1,
                                                                                     0, chr_to_replace='-')
                    elif chr_go == 'W':
                        players_hero[id_hero].wood += random.randrange(1, 4)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 1,
                                                                                     0, chr_to_replace='-')
                    elif chr_go == 'R':
                        players_hero[id_hero].rock += random.randrange(1, 4)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 1,
                                                                                     0, chr_to_replace='-')
                    elif chr_go == 'M':
                        players_hero[id_hero].cristal += random.randrange(1, 3)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 1,
                                                                                     0, chr_to_replace='-')
                    elif any(chr_go == i for i in 'OKIF'):
                        steps_current_hero, players_hero[id_hero] = list(visit_the_building(steps_current_hero, 1, 0,
                                                                                            chr_go,
                                                                                            players_hero[id_hero]))
                    elif any(chr_go == i for i in '12345'):
                        map, steps_current_hero, current_fog, cam_y, cam_x, players_hero[id_hero] = take_the_artifact(
                            map, steps_current_hero, current_fog, cam_y, cam_x, 1, 0, players_hero[id_hero], chr_go,
                            chr_to_replace='-')
                    elif chr_go == 'V':
                        preparation_window = 1, draw_preparation_window(players_hero[id_hero].slots_army,
                                                                        neutral_in_arms(neutral_dict[(
                                                                            players_hero[id_hero].y_hero + 1,
                                                                            players_hero[id_hero].x_hero)])), (1, 0)
                    elif any(chr_go == i for i in 'AB'):
                        preparation_window = 2, draw_preparation_window(players_hero[id_hero].slots_army,
                                                                        players_hero[::-1][id_hero].slots_army), (1, 0)
                elif (e.key == pygame.K_LEFT or e.key == pygame.K_KP4) and steps_current_hero:
                    chr_go = map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero - 1]
                    if chr_go == '-':
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 0,
                                                                                     -1)
                    elif chr_go == 'G':
                        players_hero[id_hero].gold += random.randrange(1000, 2001, 1000)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 0,
                                                                                     -1, chr_to_replace='-')
                    elif chr_go == 'W':
                        players_hero[id_hero].wood += random.randrange(1, 4)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 0,
                                                                                     -1, chr_to_replace='-')
                    elif chr_go == 'R':
                        players_hero[id_hero].rock += random.randrange(1, 4)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 0,
                                                                                     -1, chr_to_replace='-')
                    elif chr_go == 'M':
                        players_hero[id_hero].cristal += random.randrange(1, 3)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 0,
                                                                                     -1, chr_to_replace='-')
                    elif chr_go == 'C':
                        players_hero[id_hero].rock += random.randrange(1, 3)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 0,
                                                                                     -1, chr_to_replace='-')
                    elif any(chr_go == i for i in 'OKIF'):
                        steps_current_hero, players_hero[id_hero] = list(visit_the_building(steps_current_hero, 0, -1,
                                                                                            chr_go,
                                                                                            players_hero[id_hero]))
                    elif any(chr_go == i for i in '12345'):
                        map, steps_current_hero, current_fog, cam_y, cam_x, players_hero[id_hero] = take_the_artifact(
                            map, steps_current_hero, current_fog, cam_y, cam_x, 0, -1, players_hero[id_hero], chr_go,
                            chr_to_replace='-')
                    elif chr_go == 'V':
                        preparation_window = 1, draw_preparation_window(players_hero[id_hero].slots_army,
                                                                        neutral_in_arms(neutral_dict[(
                                                                            players_hero[id_hero].y_hero,
                                                                            players_hero[id_hero].x_hero - 1)])), (
                                                 0, -1)
                    elif any(chr_go == i for i in 'AB'):
                        preparation_window = 2, draw_preparation_window(players_hero[id_hero].slots_army,
                                                                        players_hero[::-1][id_hero].slots_army), (0, -1)
                elif (e.key == pygame.K_RIGHT or e.key == pygame.K_KP6) and steps_current_hero:

                    chr_go = map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero + 1]
                    if chr_go == '-':
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 0, 1)
                    elif chr_go == 'G':
                        players_hero[id_hero].gold += random.randrange(1000, 2001, 1000)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 0,
                                                                                     1, chr_to_replace='-')
                    elif chr_go == 'W':
                        players_hero[id_hero].wood += random.randrange(1, 4)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 0,
                                                                                     1, chr_to_replace='-')
                    elif chr_go == 'R':
                        players_hero[id_hero].rock += random.randrange(1, 4)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 0,
                                                                                     1, chr_to_replace='-')
                    elif chr_go == 'M':
                        players_hero[id_hero].cristal += random.randrange(1, 3)
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 0,
                                                                                     1, chr_to_replace='-')
                    elif any(chr_go == i for i in 'OKIF'):
                        steps_current_hero, players_hero[id_hero] = list(visit_the_building(steps_current_hero, 0, 1,
                                                                                            chr_go,
                                                                                            players_hero[id_hero]))
                    elif any(chr_go == i for i in '12345'):
                        map, steps_current_hero, current_fog, cam_y, cam_x, players_hero[id_hero] = take_the_artifact(
                            map, steps_current_hero, current_fog, cam_y, cam_x, 0, 1, players_hero[id_hero], chr_go,
                            chr_to_replace='-')
                    elif chr_go == 'V':
                        preparation_window = 1, draw_preparation_window(players_hero[id_hero].slots_army,
                                                                        neutral_in_arms(neutral_dict[(
                                                                            players_hero[id_hero].y_hero,
                                                                            players_hero[id_hero].x_hero + 1)])), (0, 1)
                    elif any(chr_go == i for i in 'AB'):
                        preparation_window = 2, draw_preparation_window(players_hero[id_hero].slots_army,
                                                                        players_hero[::-1][id_hero].slots_army), (0, 1)

            if not preparation_window[0]:
                for button in buttons:
                    button.handle_event(e)
            else:
                for b in buttons_board:
                    b.handle_event(e)
            if e.type == pygame.USEREVENT:
                if e.button == buttons[0] and not preparation_window[0]:
                    switch_scene(hero_characteristics)
                    running = False
                elif e.button == buttons[1] and not preparation_window[0]:
                    sum_day += 0.5
                    flag_player = not flag_player
                    cam_y, cam_x = (i * tile_size - ii // 2 for i, ii in
                                    zip(players_hero[::-1][id_hero].give_hero_coords(), res[::-1]))
                    steps_current_hero = players_hero[::-1][id_hero].give_hero_steps()
                    if not flag_player:
                        one_player_fog_war = current_fog[:]
                        current_fog = two_player_fog_war[:]
                    else:
                        two_player_fog_war = current_fog[:]
                        current_fog = one_player_fog_war[:]
                elif e.button == buttons[2] and not preparation_window[0]:
                    switch_scene(basic_menu_draw)
                    running = False
                elif e.button == buttons[3] and not preparation_window[0]:
                    print(4)
                elif e.button == buttons_board[0] and preparation_window[0]:
                    if preparation_window[0] == 1:
                        result = battle_enemis_scoring(players_hero[id_hero].slots_army, (
                            players_hero[id_hero].attack, players_hero[id_hero].protection,
                            players_hero[id_hero].inspiration, players_hero[id_hero].luck), neutral_dict[
                                                           (players_hero[id_hero].y_hero + preparation_window[2][0],
                                                            players_hero[id_hero].x_hero + preparation_window[2][1])])
                        if result[0]:
                            players_hero[id_hero].give_exp(result[2])
                            players_hero[id_hero].slots_army = result[1]
                            map[players_hero[id_hero].y_hero + preparation_window[2][0]][
                                players_hero[id_hero].x_hero + preparation_window[2][1]], \
                            map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero] = \
                                map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero], '-'
                            players_hero[id_hero].set_hero_coords(
                                players_hero[id_hero].y_hero + preparation_window[2][0],
                                players_hero[id_hero].x_hero + preparation_window[2][1])
                            current_fog = change_fog_war(map, current_fog, players_hero[id_hero].chr)

                            preparation_window = 0, load_image('sheaf_spears.jpg'), (0, 0)

                        else:
                            switch_scene(result_window)
                            winner = players_hero[::-1][id_hero].chr
                            running = False
                    elif preparation_window[0] == 2:
                        result = battle_enemis_hero_scoring(players_hero[id_hero].slots_army, (
                            players_hero[id_hero].attack, players_hero[id_hero].protection,
                            players_hero[id_hero].inspiration, players_hero[id_hero].luck),
                                                            players_hero[::-1][id_hero].slots_army, additional_e=(
                                players_hero[::-1][id_hero].attack, players_hero[::-1][id_hero].protection,
                                players_hero[::-1][id_hero].inspiration, players_hero[::-1][id_hero].luck))
                        if result[0]:
                            switch_scene(result_window)
                            winner = players_hero[id_hero].chr
                            running = False
                        else:
                            switch_scene(result_window)
                            winner = players_hero[::-1][id_hero].chr
                            running = False
                elif e.button == buttons_board[1] and preparation_window[0]:
                    preparation_window = 0, load_image('sheaf_spears.jpg'), (0, 0)

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            cam_x -= 3
        if key[pygame.K_d]:
            cam_x += 3
        if key[pygame.K_w]:
            cam_y -= 3
        if key[pygame.K_s]:
            cam_y += 3

        for i in chunks_on_screen((cam_x, cam_y), chunk_size, tile_size, res, (world_size_chunk_x, world_size_chunk_y)):
            chunks[i].render(current_fog)

        if not preparation_window[0]:
            for button in buttons:
                button.check_hover([int(i * (res[n] / size[n])) for n, i in enumerate(pygame.mouse.get_pos())])
                button.draw(screen)

        screen = resources_on_screen(screen, players_hero[id_hero].give_resources(), steps_current_hero,
                                     int(res[0] * 0.03), int(res[1] * 0.03), int(res[0] * 0.7), int(res[1] * 0.15),
                                     scroll, sps_resources_img)
        if preparation_window[0]:
            screen.blit(pygame.transform.scale(preparation_window[1], (int(res[0] * 0.75), int(res[1] * 0.8))),
                        (int(res[0] * 0.12), int(res[1] * 0.12)))
            for b in buttons_board:
                b.check_hover([int(i * (res[n] / size[n])) for n, i in enumerate(pygame.mouse.get_pos())])
                b.draw(screen)

        window.blit(pygame.transform.scale(screen, size), (0, 0))
        screen.blit(pygame.transform.scale(window, size), (0, 0))
        pygame.display.update()
        clock.tick(480)

        frame += 1

        if frame % 4 == 0:
            for i in range(len(sprites_enemies)):
                sprites_enemies[i].update()
            if flag_player:
                hero1_animated.update()
            else:
                hero2_animated.update()

        if frame % 100 == 0:
            pygame.display.set_caption('FPS: ' + str(round(clock.get_fps())))
            chunks_on_screen((cam_x, cam_y), chunk_size, tile_size, res, (world_size_chunk_x, world_size_chunk_y))
    return link_map, (cam_x,
                      cam_y), chunk_size, tile_size, map, one_player_fog_war, two_player_fog_war, world_size_chunk_x, world_size_chunk_y, sum_day, flag_player, players_hero, steps_current_hero, current_fog, frame, winner


def hero_characteristics(*args):
    args = args[0]
    print(args)
    heroes, flag_player = args[11], args[10]
    if flag_player:
        flag_player = 0
    else:
        flag_player = 1
    global screen
    size = 1920, 1080
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    screen = pygame.display.set_mode(size)
    surface = pygame.display.get_surface()
    size = (surface.get_width(), surface.get_height())
    button = ImageButton(int(size[0] * 0.8), int(size[1] * 0.1), int(size[0] * 0.1), int(size[1] * 0.1), '',
                         'krest1.png', hover_image_path='krest2.png')
    running = True
    screen.blit(load_image(image), (0, 0))
    while running:
        for e in pygame.event.get():
            button.handle_event(e)
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    switch_scene(None)
            if e.type == pygame.USEREVENT:
                if e.button == button:
                    running = False
                    switch_scene(game_world_draw)
                    return args[0]
        button.check_hover(pygame.mouse.get_pos())
        screen.blit(load_image(image), (0, 0))
        button.check_hover(pygame.mouse.get_pos())

        board = load_image('board.png', colorkey=-1)
        screen.blit(
                pygame.transform.scale(board, (int(size[0] * 0.4), int(size[1] * 0.6))),
                (int(size[0] * 0.27), int(size[1] * 0.25)))

        m_arm = load_image('12620557_4Z_2101.w017.n001.350A.p30.350.png', colorkey=-1)

        s = [load_image('sword.png', colorkey=-1),
             load_image('sheet.png', colorkey=-1),
             load_image('luck.png', colorkey=-1),
             load_image('flagg.png', colorkey=-1)]
        for x, ii, img in zip(range(30, 66, 10), range(1, 5), range(4)):

            screen.blit(
                pygame.transform.scale(m_arm, (int(size[0] * 0.05), int(size[0] * 0.05))),
                (int(size[0] * (x + 1) // 100), int(size[1] * 0.4)))
            screen.blit(
                pygame.transform.scale(s[img], (int(size[0] * 0.05 * 0.8), int(size[0] * 0.05 * 0.7))),
                (int(size[0] * (x + 1.5) // 100), int(size[1] * 0.42)))
            font = pygame.font.Font(None, 50)
            text_surface = font.render(str(heroes[flag_player].give_characteristics()[ii - 1]), True, (218, 165, 32))
            screen.blit(text_surface, (int(size[0] * (x + 2) / 100), int(size[1] * (40 + 5) / 100)))

        army = list(heroes[flag_player].slots_army)
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

        for y, i in zip(range(60, 71, 10), range(1, 3)):
            for x, ii in zip(range(35, 71, 10), range(1, 4)):
                screen.blit(
                    pygame.transform.scale(m_arm,
                                           (int(size[0] * 0.05), int(size[0] * 0.05))),
                    (int(size[0] * x // 100), int(size[1] * y // 100)))
                if army[i * ii - 1]:
                    screen.blit(
                        pygame.transform.scale(d[army[i * ii - 1][0].name],
                                               (int(size[0] * 0.05 * 0.95), int(size[0] * 0.05 * 0.95))),
                        (int(size[0] * (x / 100)), int(size[1] * (y / 100))))
                    font = pygame.font.Font(None, 50)
                    text_surface = font.render(str(army[i * ii - 1][1]), True, (218, 165, 32))
                    screen.blit(text_surface, (int(size[0] * (x + 2) / 100), int(size[1] * (y + 5) / 100)))

        button.draw(screen)
        pygame.display.flip()
    return args


def result_window(*args):
    args = args[0]
    day, heroes, winner = args[9], args[11], args[15]
    global screen
    size = [1920, 1080]
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    screen = pygame.display.set_mode(size)
    surface = pygame.display.get_surface()
    size = (surface.get_width(), surface.get_height())
    button = ImageButton(int(size[0] * 0.8), int(size[1] * 0.1), int(size[0] * 0.1), int(size[1] * 0.1), '',
                         'krest1.png', hover_image_path='krest2.png')

    running = True
    screen.blit(load_image(image), (0, 0))
    while running:
        for e in pygame.event.get():
            button.handle_event(e)
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    switch_scene(None)
            if e.type == pygame.USEREVENT:
                if e.button == button:
                    running = False
                    switch_scene(basic_menu_draw)
                    return args[0]

        button.check_hover(pygame.mouse.get_pos())
        screen.blit(load_image(image), (0, 0))
        button.check_hover(pygame.mouse.get_pos())

        m_arm = load_image('12620557_4Z_2101.w017.n001.350A.p30.350.png', colorkey=-1)
        if winner == 'A':
            screen.blit(
                pygame.transform.scale(load_image('winner.png', colorkey=-1),
                                       (int(size[0] * 0.1), int(size[0] * 0.1))),
                (int(size[0] * 0.2), int(size[1] * 0.1)))
        else:
            screen.blit(
                pygame.transform.scale(load_image('winner.png', colorkey=-1), (int(size[0] * 0.1), int(size[0] * 0.1))),
                (int(size[0] * 0.7), int(size[1] * 0.1)))

        s = [load_image('sword.png', colorkey=-1),
             load_image('sheet.png', colorkey=-1),
             load_image('luck.png', colorkey=-1),
             load_image('flagg.png', colorkey=-1)]
        for i, pr in zip(range(2), (0, 40)):
            for x, ii, img in zip(range(10, 46, 10), range(1, 5), range(4)):
                screen.blit(
                    pygame.transform.scale(m_arm, (int(size[0] * 0.05), int(size[0] * 0.05))),
                    (int(size[0] * (x + pr + 1) // 100), int(size[1] * 0.4)))
                screen.blit(
                    pygame.transform.scale(s[img], (int(size[0] * 0.05 * 0.8), int(size[0] * 0.05 * 0.7))),
                    (int(size[0] * (x + pr + 1.5) // 100), int(size[1] * 0.42)))
                font = pygame.font.Font(None, 50)
                text_surface = font.render(str(heroes[i].give_characteristics()[ii - 1]), True, (218, 165, 32))
                screen.blit(text_surface, (int(size[0] * (x + 2 + pr) / 100), int(size[1] * (40 + 5) / 100)))

        army1 = list(heroes[0].slots_army)
        army2 = list(heroes[1].slots_army)
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

        for y, i in zip(range(70, 81, 10), range(1, 3)):
            for x, ii in zip(range(10, 36, 10), range(1, 4)):
                screen.blit(
                    pygame.transform.scale(m_arm,
                                           (int(size[0] * 0.05), int(size[0] * 0.05))),
                    (int(size[0] * x // 100), int(size[1] * y // 100)))
                if army1[i * ii - 1]:
                    screen.blit(
                        pygame.transform.scale(d[army1[i * ii - 1][0].name],
                                               (int(size[0] * 0.05 * 0.95), int(size[0] * 0.05 * 0.95))),
                        (int(size[0] * (x / 100)), int(size[1] * (y / 100))))
                    font = pygame.font.Font(None, 50)
                    text_surface = font.render(str(army1[i * ii - 1][1]), True, (218, 165, 32))
                    screen.blit(text_surface, (int(size[0] * (x + 2) / 100), int(size[1] * (y + 5) / 100)))
            for x, ii in zip(range(60, 81, 10), range(1, 4)):
                screen.blit(
                    pygame.transform.scale(m_arm,
                                           (int(size[0] * 0.05), int(size[0] * 0.05))),
                    (int(size[0] * x // 100), int(size[1] * y // 100)))
                if army2[i * ii - 1]:
                    screen.blit(
                        pygame.transform.scale(d[army2[i * ii - 1][0].name],
                                               (int(size[0] * 0.05 * 0.95), int(size[0] * 0.05 * 0.95))),
                        (int(size[0] * (x / 100)), int(size[1] * (y / 100))))
                    font = pygame.font.Font(None, 50)
                    text_surface = font.render(str(army2[i * ii - 1][1]), True, (218, 165, 32))
                    screen.blit(text_surface, (int(size[0] * (x + 2) / 100), int(size[1] * (y + 5) / 100)))
        button.draw(screen)
        pygame.display.flip()


def castle_draw(user_id, can_add_new_building, hero_in_castle=False):
    # user_id = 0
    # can_add_new_building = 0
    # hero_in_castle = False
    icon_width = 125
    icon_height = 155
    db = "GameDB.db3"
    db = os.path.join('data/db', db)
    con = sqlite3.connect(db)
    list_l = ['lvl', 'horse_stable', 'marketplace', 'militia', 'pennies', 'swordmans', 'knights', 'archer',
              'crossbowman', 'cleric', 'abbot', 'angel', 'horseman']

    def load_data():
        if user_id == 2:
            castle_buying_id = 7
            castle_army_id = 4
        elif user_id == 2:
            castle_buying_id = 8
            castle_army_id = 6
        cur = con.cursor()
        units = cur.execute("""SELECT unit_name FROM units """).fetchall()
        buying_values = []
        army_values = []
        for i in units:
            unit = i[0]
            buying = cur.execute(f"""SELECT {unit} FROM army WHERE id = {castle_buying_id}""").fetchone()
            army = cur.execute(f"""SELECT {unit} FROM army WHERE id = {castle_army_id}""").fetchone()
            buying_values.append(buying[0])
            army_values.append(army[0])

        values = [[pygame.font.SysFont('arial', 30).render(f'{buying_values[0]}', True, (255, 255, 255)),
                   (1343, 180)],
                  [pygame.font.SysFont('arial', 30).render(f'{buying_values[1]}', True, (255, 255, 255)),
                   (1493, 180)],
                  [pygame.font.SysFont('arial', 30).render(f'{buying_values[2]}', True, (255, 255, 255)),
                   (1343, 380)],
                  [pygame.font.SysFont('arial', 30).render(f'{buying_values[3]}', True, (255, 255, 255)),
                   (1493, 380)],
                  [pygame.font.SysFont('arial', 30).render(f'{buying_values[4]}', True, (255, 255, 255)),
                   (1343, 580)],
                  [pygame.font.SysFont('arial', 30).render(f'{buying_values[5]}', True, (255, 255, 255)),
                   (1493, 580)],
                  [pygame.font.SysFont('arial', 30).render(f'{buying_values[6]}', True, (255, 255, 255)),
                   (1343, 780)],
                  [pygame.font.SysFont('arial', 30).render(f'{buying_values[7]}', True, (255, 255, 255)),
                   (1493, 780)],
                  [pygame.font.SysFont('arial', 30).render(f'{buying_values[8]}', True, (255, 255, 255)),
                   (1343, 980)],
                  [pygame.font.SysFont('arial', 30).render(f'{buying_values[9]}', True, (255, 255, 255)),
                   (1493, 980)],

                  [pygame.font.SysFont('arial', 30).render(f'{army_values[0]}', True, (255, 255, 255)),
                   (1688, 180)],
                  [pygame.font.SysFont('arial', 30).render(f'{army_values[1]}', True, (255, 255, 255)),
                   (1838, 180)],
                  [pygame.font.SysFont('arial', 30).render(f'{army_values[2]}', True, (255, 255, 255)),
                   (1688, 380)],
                  [pygame.font.SysFont('arial', 30).render(f'{army_values[3]}', True, (255, 255, 255)),
                   (1838, 380)],
                  [pygame.font.SysFont('arial', 30).render(f'{army_values[4]}', True, (255, 255, 255)),
                   (1688, 580)],
                  [pygame.font.SysFont('arial', 30).render(f'{army_values[5]}', True, (255, 255, 255)),
                   (1838, 580)],
                  [pygame.font.SysFont('arial', 30).render(f'{army_values[6]}', True, (255, 255, 255)),
                   (1688, 780)],
                  [pygame.font.SysFont('arial', 30).render(f'{army_values[7]}', True, (255, 255, 255)),
                   (1838, 780)],
                  [pygame.font.SysFont('arial', 30).render(f'{army_values[8]}', True, (255, 255, 255)),
                   (1688, 980)],
                  [pygame.font.SysFont('arial', 30).render(f'{army_values[9]}', True, (255, 255, 255)),
                   (1838, 980)]
                  ]
        return values

    def load_building():
        cur = con.cursor()
        building = {}
        castle = cur.execute("""SELECT lvl, horse_stable, marketplace, militia, pennies, swordmans, knights, 
        archer, crossbowman, cleric, abbot, angel, horseman FROM castles 
        WHERE id = ?""", (user_id,)).fetchone()
        for i in range(len(list_l)):
            building[list_l[i]] = castle[i]
        return building

    buttons = [ImageButton(1280, 25, icon_width, icon_height, '', 'krestianin_ikonka.png',
                           hover_image_path='krestianin_ikonka.png'),
               ImageButton(1430, 25, icon_width, icon_height, '', 'kopeishik_ikonka.png',
                           hover_image_path='kopeishik_ikonka.png'),
               ImageButton(1280, 225, icon_width, icon_height, '', 'mechnik_ikonka.png',
                           hover_image_path='mechnik_ikonka.png'),
               ImageButton(1430, 225, icon_width, icon_height, '', 'knight_ikonka.png',
                           hover_image_path='knight_ikonka.png'),
               ImageButton(1280, 425, icon_width, icon_height, '', 'luchnick_ikonka.png',
                           hover_image_path='luchnick_ikonka.png'),
               ImageButton(1430, 425, icon_width, icon_height, '', 'arbaletchik_ikonka.png',
                           hover_image_path='arbaletchik_ikonka.png'),
               ImageButton(1280, 625, icon_width, icon_height, '', 'clerick_ikonka.png',
                           hover_image_path='clerick_ikonka.png'),
               ImageButton(1430, 625, icon_width, icon_height, '', 'abbot_ikonka.png',
                           hover_image_path='abbot_ikonka.png'),
               ImageButton(1280, 825, icon_width, icon_height, '', 'angel_ikonka.png',
                           hover_image_path='angel_ikonka.png'),
               ImageButton(1430, 825, icon_width, icon_height, '', 'vsadnik_ikonka.png',
                           hover_image_path='vsadnik_ikonka.png'),

               ImageButton(1625, 25, icon_width, icon_height, '', 'krestianin_ikonka.png',
                           hover_image_path='krestianin_ikonka.png'),
               ImageButton(1775, 25, icon_width, icon_height, '', 'kopeishik_ikonka.png',
                           hover_image_path='kopeishik_ikonka.png'),
               ImageButton(1625, 225, icon_width, icon_height, '', 'mechnik_ikonka.png',
                           hover_image_path='mechnik_ikonka.png'),
               ImageButton(1775, 225, icon_width, icon_height, '', 'knight_ikonka.png',
                           hover_image_path='knight_ikonka.png'),
               ImageButton(1625, 425, icon_width, icon_height, '', 'luchnick_ikonka.png',
                           hover_image_path='luchnick_ikonka.png'),
               ImageButton(1775, 425, icon_width, icon_height, '', 'arbaletchik_ikonka.png',
                           hover_image_path='arbaletchik_ikonka.png'),
               ImageButton(1625, 625, icon_width, icon_height, '', 'clerick_ikonka.png',
                           hover_image_path='clerick_ikonka.png'),
               ImageButton(1775, 625, icon_width, icon_height, '', 'abbot_ikonka.png',
                           hover_image_path='abbot_ikonka.png'),
               ImageButton(1625, 825, icon_width, icon_height, '', 'angel_ikonka.png',
                           hover_image_path='angel_ikonka.png'),
               ImageButton(1775, 825, icon_width, icon_height, '', 'vsadnik_ikonka.png',
                           hover_image_path='vsadnik_ikonka.png'),

               ImageButton(1025, 845, 200, 200, '', 'coin_ikonka.png',
                           hover_image_path='coin_ikonka.png'),

               ImageButton(220, 210, 200, 200, '', 'sheaf_spears.jpg',
                           hover_image_path='sheaf_spears.jpg'),
               ImageButton(220, 420, 200, 200, '', 'knight_buying_ikonka.jpg',
                           hover_image_path='knight_buying_ikonka.jpg'),
               ImageButton(530, 210, 200, 200, '', 'coin_ikonka.png',
                           hover_image_path='coin_ikonka.png'),
               ImageButton(840, 210, 200, 200, '', 'coin_ikonka.png',
                           hover_image_path='coin_ikonka.png'),
               ImageButton(530, 420, 200, 200, '', 'coin_ikonka.png',
                           hover_image_path='coin_ikonka.png'),
               ImageButton(840, 420, 200, 200, '', 'coin_ikonka.png',
                           hover_image_path='coin_ikonka.png'),
               ImageButton(220, 630, 200, 200, '', 'coin_ikonka.png',
                           hover_image_path='coin_ikonka.png'),
               ImageButton(530, 630, 200, 200, '', 'coin_ikonka.png',
                           hover_image_path='coin_ikonka.png'),
               ImageButton(840, 630, 200, 200, '', 'coin_ikonka.png',
                           hover_image_path='coin_ikonka.png'),

               ImageButton(0, 210, 200, 200, '', 'lvl_1_ikonka.png',
                           hover_image_path='lvl_1_ikonka.png'),
               ImageButton(0, 420, 200, 200, '', 'lvl_2_ikonka.png',
                           hover_image_path='lvl_2_ikonka.png'),
               ImageButton(0, 630, 200, 200, '', 'lvl_3_ikonka.png',
                           hover_image_path='lvl_3_ikonka.png'),

               ImageButton(0, 0, 200, 100, 'Exit',
                           '—Pngtree—buttons games button illustration_5544907.png',
                           hover_image_path='—Pngtree—buttons games button illustration_5544907_2.png')
               ]
    text = [[pygame.font.SysFont('arial', 44).render('Армия', True, (255, 255, 255)),
             (1280, 1025)],
            [pygame.font.SysFont('arial', 44).render('Покупка армии', True, (255, 255, 255)),
             (1625, 1025)]]
    value_text = load_data()
    building_value = load_building()
    icon_selected = False
    chosen_unit = chosen_unit_rus = ''
    chosen_building = chosen_building_rus = ''
    running = True
    while running:
        screen.blit(load_image(image), (0, 0))
        pygame.draw.rect(screen, (82, 122, 149), (1260, 0, 660, 1080))
        pygame.draw.rect(screen, (138, 6, 0), (0, 830, 1260, 270))
        pygame.draw.rect(screen, (255, 191, 26), (1580, 0, 20, 1080))
        pygame.draw.rect(screen, (255, 191, 26), (1240, 0, 20, 1080))
        pygame.draw.rect(screen, (255, 191, 26), (0, 200, 1260, 10))
        pygame.draw.rect(screen, (255, 191, 26), (0, 410, 1260, 10))
        pygame.draw.rect(screen, (255, 191, 26), (0, 620, 1260, 10))
        pygame.draw.rect(screen, (255, 191, 26), (0, 830, 1260, 10))
        for text_massage in text:
            screen.blit(text_massage[0], text_massage[1])
        for value in value_text:
            screen.blit(value[0], value[1])
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            #   switch_scene(None)
            for button in buttons:
                button.handle_event(e)
            if e.type == pygame.USEREVENT:
                if e.button == buttons[0] and hero_in_castle:
                    if user_id == 2:
                        r = RedCastle()
                        r.add_army_to_hero('peasant')
                    elif user_id == 3:
                        b = BlueCastle()
                        b.add_army_to_hero('peasant')
                elif e.button == buttons[1] and hero_in_castle:
                    if user_id == 2:
                        r = RedCastle()
                        r.add_army_to_hero('penny')
                    elif user_id == 3:
                        b = BlueCastle()
                        b.add_army_to_hero('penny')
                elif e.button == buttons[2] and hero_in_castle:
                    if user_id == 2:
                        r = RedCastle()
                        r.add_army_to_hero('swordman')
                    elif user_id == 3:
                        b = BlueCastle()
                        b.add_army_to_hero('swordman')
                elif e.button == buttons[3] and hero_in_castle:
                    if user_id == 2:
                        r = RedCastle()
                        r.add_army_to_hero('knight')
                    elif user_id == 3:
                        b = BlueCastle()
                        b.add_army_to_hero('knight')
                elif e.button == buttons[4] and hero_in_castle:
                    if user_id == 2:
                        r = RedCastle()
                        r.add_army_to_hero('archer')
                    elif user_id == 3:
                        b = BlueCastle()
                        b.add_army_to_hero('archer')
                elif e.button == buttons[5] and hero_in_castle:
                    if user_id == 2:
                        r = RedCastle()
                        r.add_army_to_hero('crossbowman')
                    elif user_id == 3:
                        b = BlueCastle()
                        b.add_army_to_hero('crossbowman')
                elif e.button == buttons[6] and hero_in_castle:
                    if user_id == 2:
                        r = RedCastle()
                        r.add_army_to_hero('cleric')
                    elif user_id == 3:
                        b = BlueCastle()
                        b.add_army_to_hero('cleric')
                elif e.button == buttons[7] and hero_in_castle:
                    if user_id == 2:
                        r = RedCastle()
                        r.add_army_to_hero('abbot')
                    elif user_id == 3:
                        b = BlueCastle()
                        b.add_army_to_hero('abbot')
                elif e.button == buttons[8] and hero_in_castle:
                    if user_id == 2:
                        r = RedCastle()
                        r.add_army_to_hero('angel')
                    elif user_id == 3:
                        b = BlueCastle()
                        b.add_army_to_hero('angel')
                elif e.button == buttons[9] and hero_in_castle:
                    if user_id == 2:
                        r = RedCastle()
                        r.add_army_to_hero('horseman')
                    elif user_id == 3:
                        b = BlueCastle()
                        b.add_army_to_hero('horseman')

                elif e.button == buttons[10]:
                    chosen_unit = 'peasant'
                    chosen_unit_rus = 'Крестьянин'
                    chosen_building = chosen_building_rus = ''
                    icon_selected = True
                elif e.button == buttons[11]:
                    chosen_unit = 'penny'
                    chosen_unit_rus = 'Копейщик'
                    chosen_building = chosen_building_rus = ''
                    icon_selected = True
                elif e.button == buttons[12]:
                    chosen_unit = 'swordman'
                    chosen_unit_rus = 'Мечник'
                    chosen_building = chosen_building_rus = ''
                    icon_selected = True
                elif e.button == buttons[13]:
                    chosen_unit = 'knight'
                    chosen_unit_rus = 'Рыцарь'
                    chosen_building = chosen_building_rus = ''
                    icon_selected = True
                elif e.button == buttons[14]:
                    chosen_unit = 'archer'
                    chosen_unit_rus = 'Лучник'
                    chosen_building = chosen_building_rus = ''
                    icon_selected = True
                elif e.button == buttons[15]:
                    chosen_unit = 'crossbowman'
                    chosen_unit_rus = 'Стрелок'
                    chosen_building = chosen_building_rus = ''
                    icon_selected = True
                elif e.button == buttons[16]:
                    chosen_unit = 'cleric'
                    chosen_unit_rus = 'Клирик'
                    chosen_building = chosen_building_rus = ''
                    icon_selected = True
                elif e.button == buttons[17]:
                    chosen_unit = 'abbot'
                    chosen_unit_rus = 'Аббат'
                    chosen_building = chosen_building_rus = ''
                    icon_selected = True
                elif e.button == buttons[18]:
                    chosen_unit = 'angel'
                    chosen_unit_rus = 'Ангел'
                    chosen_building = chosen_building_rus = ''
                    icon_selected = True
                elif e.button == buttons[19]:
                    chosen_unit = 'horseman'
                    chosen_unit_rus = 'Всадник'
                    chosen_building = chosen_building_rus = ''
                    icon_selected = True

                elif e.button == buttons[20]:
                    if chosen_unit != '' and chosen_building == '':
                        if user_id == 2:
                            r = RedCastle()
                            r.buy_army(chosen_unit)
                            load_data()
                        elif user_id == 3:
                            b = BlueCastle()
                            b.buy_army(chosen_unit)
                            load_data()
                        can_add_new_building = False
                    elif chosen_unit == '' and (chosen_building != '' and chosen_building != 'lvl2'
                                                and chosen_building != 'lvl3') and can_add_new_building:
                        if user_id == 2:
                            r = RedCastle()
                            r.new_building(chosen_building)
                            load_building()
                        elif user_id == 3:
                            b = BlueCastle()
                            b.new_building(chosen_building)
                            load_building()
                        can_add_new_building = False
                    elif chosen_unit == '' and chosen_building == 'lvl2':
                        if user_id == 2:
                            r = RedCastle()
                            r.update_castle()
                            load_building()
                        elif user_id == 3:
                            b = BlueCastle()
                            b.update_castle()
                            load_building()
                        can_add_new_building = False
                    elif chosen_unit == '' and chosen_building == 'lvl3':
                        if user_id == 2:
                            r = RedCastle()
                            r.update_castle()
                            load_building()
                        elif user_id == 3:
                            b = BlueCastle()
                            b.update_castle()
                            load_building()
                        can_add_new_building = False

                elif e.button == buttons[21]:
                    chosen_building = 'pennies'
                    chosen_building_rus = 'Казармы копейщиков'
                    chosen_unit = chosen_unit_rus = ''
                    icon_selected = True
                elif e.button == buttons[22]:
                    chosen_building = 'knights'
                    chosen_building_rus = 'Рыцарский замок'
                    chosen_unit = chosen_unit_rus = ''
                    icon_selected = True
                elif e.button == buttons[23]:
                    chosen_building = 'marketplace'
                    chosen_building_rus = 'Рынок'
                    chosen_unit = chosen_unit_rus = ''
                    icon_selected = True
                elif e.button == buttons[24]:
                    chosen_building = 'crossbowman'
                    chosen_building_rus = 'Плац стрелков'
                    chosen_unit = chosen_unit_rus = ''
                    icon_selected = True
                elif e.button == buttons[25]:
                    chosen_building = 'cleric'
                    chosen_building_rus = 'Молебни'
                    chosen_unit = chosen_unit_rus = ''
                    icon_selected = True
                elif e.button == buttons[26]:
                    chosen_building = 'horse_stable'
                    chosen_building_rus = 'Конная разведка'
                    chosen_unit = chosen_unit_rus = ''
                    icon_selected = True
                elif e.button == buttons[27]:
                    chosen_building = 'abbot'
                    chosen_building_rus = 'Собор'
                    chosen_unit = chosen_unit_rus = ''
                    icon_selected = True
                elif e.button == buttons[28]:
                    chosen_building = 'angel'
                    chosen_building_rus = 'Небесный алтарь'
                    chosen_unit = chosen_unit_rus = ''
                    icon_selected = True
                elif e.button == buttons[29]:
                    chosen_building = 'horseman'
                    chosen_building_rus = 'Конные мастера'
                    chosen_unit = chosen_unit_rus = ''
                    icon_selected = True

                elif e.button == buttons[30]:
                    chosen_building = 'lvl1'
                    chosen_building_rus = 'Уровень замка 1'
                    chosen_unit = chosen_unit_rus = ''
                    icon_selected = True
                elif e.button == buttons[31]:
                    chosen_building = 'lvl2'
                    chosen_building_rus = 'Уровень замка 2'
                    chosen_unit = chosen_unit_rus = ''
                    icon_selected = True
                elif e.button == buttons[32]:
                    chosen_building = 'lvl3'
                    chosen_building_rus = 'Уровень замка 3'
                    chosen_unit = chosen_unit_rus = ''
                    icon_selected = True

                elif e.button == buttons[33]:
                    switch_scene(game_world_draw)
                    running = False

        for button in buttons:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(screen)
        if icon_selected:
            cur = con.cursor()
            if chosen_unit != '' and chosen_building == '':
                price = cur.execute("""SELECT price FROM units WHERE unit_name = ?""",
                                    (chosen_unit,)).fetchone()
                description = f'{chosen_unit_rus}: стоимость - {price[0]} золота'
                t = pygame.font.SysFont('arial', 45).render(description, True, (255, 255, 255))
                screen.blit(t, (20, 850))
            elif chosen_unit == '' and chosen_building == 'lvl1':
                description = f'{chosen_building_rus}: здание уже построено'
                t = pygame.font.SysFont('arial', 35).render(description, True, (255, 255, 255))
                screen.blit(t, (20, 850))
            elif chosen_unit == '' and chosen_building != '' and building_value['lvl'] == 1:
                price = cur.execute("""SELECT gold, wood, rock, magic_cristalls FROM castle_units 
                                                    WHERE name = ?""", (chosen_building,)).fetchone()
                description = (f'{chosen_building_rus}: стоимость - {price[0]} золота, {price[1]} дерева, '
                               f'{price[2]} камня, {price[3]} магических кристаллов')
                t = pygame.font.SysFont('arial', 35).render(description, True, (255, 255, 255))
                screen.blit(t, (20, 850))
            elif chosen_unit == '' and chosen_building != '' and building_value['lvl'] == 2:
                price = cur.execute("""SELECT gold, wood, rock, magic_cristalls FROM castle_units 
                                                    WHERE name = ?""", (chosen_building,)).fetchone()
                description = (f'{chosen_building_rus}: стоимость - {price[0]} золота, {price[1]} дерева, '
                               f'{price[2]} камня, {price[3]} магических кристаллов')
                t = pygame.font.SysFont('arial', 35).render(description, True, (255, 255, 255))
                screen.blit(t, (20, 850))
            elif chosen_unit == '' and chosen_building != '' and building_value[chosen_building] == 'no':
                price = cur.execute("""SELECT gold, wood, rock, magic_cristalls FROM castle_units 
                                    WHERE name = ?""", (chosen_building,)).fetchone()
                description = (f'{chosen_building_rus}: стоимость - {price[0]} золота, {price[1]} дерева, '
                               f'{price[2]} камня, {price[3]} магических кристаллов')
                t = pygame.font.SysFont('arial', 35).render(description, True, (255, 255, 255))
                screen.blit(t, (20, 850))
            elif chosen_unit == '' and chosen_building != '' and building_value[chosen_building] == 'yes':
                description = f'{chosen_building_rus}: здание уже построено'
                t = pygame.font.SysFont('arial', 35).render(description, True, (255, 255, 255))
                screen.blit(t, (20, 850))
        pygame.display.flip()


switch_scene(game_world_draw)
data_game = 'data/maps/map_1.txt',
while current_scene is not None:
    data_game = current_scene(data_game)
pygame.quit()
