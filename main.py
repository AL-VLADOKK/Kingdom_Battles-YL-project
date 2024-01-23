from menu_start import BasicMenu
from func_load_image import load_image
from buton import ImageButton
from shablon import Hero, AnimatedSprite
from fog_war import create_fog_war, change_fog_war
from on_screen import chunks_on_screen, resources_on_screen
from neutral import create_dict_neutral
import pygame  # импорт библиотеки PyGame
import random

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
    menu.append_option('Выбрать карту', lambda: quit)
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


def game_world_draw(*args):
    args = args[0]
    flag_data = True if len(args) > 1 else False
    link_map = args[0]

    size = [1920, 1080]
    res = [480, 260]

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
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, -1, 0,
                                                                                     chr_to_replace='-')



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
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 1, 0,
                                                                                     chr_to_replace='-')

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
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 0, -1,
                                                                                     chr_to_replace='-')
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
                        map, steps_current_hero, current_fog, cam_y, cam_x = go_hero(map, steps_current_hero,
                                                                                     current_fog, cam_y, cam_x, 0, 1,
                                                                                     chr_to_replace='-')

            for button in buttons:
                button.handle_event(e)
            if e.type == pygame.USEREVENT:
                if e.button == buttons[0]:
                    switch_scene(hero_characteristics)
                    running = False
                elif e.button == buttons[1]:
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
                elif e.button == buttons[2]:
                    switch_scene(basic_menu_draw)
                    running = False
                elif e.button == buttons[3]:
                    print(4)

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

        for button in buttons:
            button.check_hover([int(i * (res[n] / size[n])) for n, i in enumerate(pygame.mouse.get_pos())])
            button.draw(screen)
        screen = resources_on_screen(screen, players_hero[id_hero].give_resources(), steps_current_hero,
                                     int(res[0] * 0.03), int(res[1] * 0.03), int(res[0] * 0.7), int(res[1] * 0.15),
                                     scroll, sps_resources_img)

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
                      cam_y), chunk_size, tile_size, map, one_player_fog_war, two_player_fog_war, world_size_chunk_x, world_size_chunk_y, sum_day, flag_player, players_hero, steps_current_hero, current_fog, frame


def hero_characteristics(*args):
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
        button.draw(screen)
        pygame.display.flip()


switch_scene(game_world_draw)
data_game = 'data/maps/map_1.txt',
while current_scene is not None:
    data_game = current_scene(data_game)
pygame.quit()
