import sqlite3
import os
from buildings import RedCastle, BlueCastle, Buildings
from menu_start import BasicMenu
from func_load_image import load_image
from buton import ImageButton
from shablon import Hero, AnimatedSprite
import pygame  # импорт библиотеки PyGame

pygame.init()  # инициализируем PyGame

WIDTH = 1920  # ширина экрана
HEIGHT = 1080  # высота экрана

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создаем поверхность экрана

current_scene = print
fon_download = 'fon_download.png'
image = "zamok_gorod_fentezi_174584_1920x1080.jpg"

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
    ret = args
    map = ret[0]

    size = [1920, 1080]
    res = [480, 260]

    cam_x, cam_y = 0, 0
    global screen
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    window = pygame.transform.scale(screen, res)
    surface = pygame.display.get_surface()
    size = [surface.get_width(), surface.get_height()]

    clock = pygame.time.Clock()

    chunk_size = 8
    tile_size = 16

    r = open(f'{map}', mode="r").readlines()
    map = [i.rstrip() + '#' * (chunk_size - len(map[0][:-3]) % chunk_size) for i in r]
    map = map + ['#' * len(map[0])] * (chunk_size - len(map) % chunk_size)
    map = [list(i) for i in map]
    one_player_fog_war = [[False for __ in _] for _ in map]
    two_player_fog_war = [[False for __ in _] for _ in map]

    world_size_chunk_x = len(map[0]) // chunk_size
    world_size_chunk_y = len(map) // chunk_size

    link_sprites_hero1 = 'hero1_standing.png'
    link_sprites_hero2 = 'hero2_standing.png'

    hero1_animated = AnimatedSprite(load_image(link_sprites_hero1, colorkey=-1), 3, 1, 19, 20)
    hero2_animated = AnimatedSprite(load_image(link_sprites_hero2, colorkey=-1), 3, 1, 19, 20)

    def chunks_on_screen(cam, chunk_size, tile_size, res, world_size_chunk):
        x1 = cam[0] // (chunk_size * tile_size)
        y1 = cam[1] // (chunk_size * tile_size)

        x2 = (cam[0] + res[0]) // (chunk_size * tile_size)
        y2 = (cam[1] + res[1]) // (chunk_size * tile_size)

        x1 = min(max(x1, 0), world_size_chunk[0] - 1)
        x2 = min(max(x2, 0), world_size_chunk[0] - 1)

        y1 = min(max(y1, 0), world_size_chunk[1] - 1)
        y2 = min(max(y2, 0), world_size_chunk[1] - 1)

        result = []
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                result.append(x + y * world_size_chunk[1])

        return result

    class Chunk:
        trava = pygame.transform.scale(
            load_image('1626746394_9-kartinkin-com-p-pikselnaya-tekstura-travi-krasivo-11.jpg'),
            (tile_size, tile_size))

        def __init__(self, coord_tiel, x, y):
            self.n_tiel_x, self.n_tiel_y = coord_tiel
            self.x, self.y = x, y

        def render(self):
            pas = (False, (0, 0))
            for y in range(chunk_size):
                for x in range(chunk_size):
                    screen.blit(Chunk.trava, (self.x + x * tile_size - cam_x, self.y + y * tile_size - cam_y))
                    key = map[self.n_tiel_y + y][self.n_tiel_x + x - 1]
                    if pas[0]:
                        key = map[self.n_tiel_y + pas[1][0]][self.n_tiel_x + pas[1][1] - 1]
                        texture = pygame.transform.scale(
                            img_objects_map[key],
                            (tile_size * 3, tile_size * 3))
                        screen.blit(texture,
                                    (self.x + (pas[1][1] - 1) * tile_size - cam_x,
                                     self.y + (pas[1][0] - 2) * tile_size - cam_y))
                        pas = (False, (0, 0))
                    elif key in 'AB':
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

    sum_day = 0
    flag_player = True

    players_hero = [Hero('A', 2), Hero('B', 3)]  # !!!!! нужно подключить армию
    players_hero[0].find_hero_coords(map)
    players_hero[1].find_hero_coords(map)
    steps_current_hero = players_hero[0 if flag_player else 1].give_hero_steps()

    frame = 0
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
                elif e.key == pygame.K_UP or e.key == pygame.K_KP8:
                    chr_go = map[players_hero[id_hero].y_hero - 1][players_hero[id_hero].x_hero]
                    if chr_go == '-' and steps_current_hero:
                        steps_current_hero -= 1
                        map[players_hero[id_hero].y_hero - 1][players_hero[id_hero].x_hero], \
                            map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero] = \
                            map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero], \
                                map[players_hero[id_hero].y_hero - 1][players_hero[id_hero].x_hero]
                        players_hero[id_hero].set_hero_coords(players_hero[id_hero].y_hero - 1,
                                                              players_hero[id_hero].x_hero)
                        if not (e.mod == pygame.KMOD_LSHIFT):
                            cam_y, cam_x = (i * tile_size - ii // 2 for i, ii in
                                            zip(players_hero[id_hero].give_hero_coords(), res[::-1]))

                elif e.key == pygame.K_DOWN or e.key == pygame.K_KP2:
                    chr_go = map[players_hero[id_hero].y_hero + 1][players_hero[id_hero].x_hero]
                    if chr_go == '-' and steps_current_hero:
                        steps_current_hero -= 1
                        map[players_hero[id_hero].y_hero + 1][players_hero[id_hero].x_hero], \
                            map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero] = \
                            map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero], \
                                map[players_hero[id_hero].y_hero + 1][players_hero[id_hero].x_hero]
                        players_hero[id_hero].set_hero_coords(players_hero[id_hero].y_hero + 1,
                                                              players_hero[id_hero].x_hero)
                        if not (e.mod == pygame.KMOD_LSHIFT):
                            cam_y, cam_x = (i * tile_size - ii // 2 for i, ii in
                                            zip(players_hero[id_hero].give_hero_coords(), res[::-1]))
                elif e.key == pygame.K_LEFT or e.key == pygame.K_KP4:
                    chr_go = map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero - 1]
                    if chr_go == '-' and steps_current_hero:
                        steps_current_hero -= 1
                        map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero - 1], \
                            map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero] = \
                            map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero], \
                                map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero - 1]
                        players_hero[id_hero].set_hero_coords(players_hero[id_hero].y_hero,
                                                              players_hero[id_hero].x_hero - 1)
                        if not (e.mod == pygame.KMOD_LSHIFT):
                            cam_y, cam_x = (i * tile_size - ii // 2 for i, ii in
                                            zip(players_hero[id_hero].give_hero_coords(), res[::-1]))

                elif e.key == pygame.K_RIGHT or e.key == pygame.K_KP6:

                    chr_go = map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero + 1]
                    if chr_go == '-' and steps_current_hero:
                        steps_current_hero -= 1
                        map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero + 1], \
                            map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero] = \
                            map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero], \
                                map[players_hero[id_hero].y_hero][players_hero[id_hero].x_hero + 1]
                        players_hero[id_hero].set_hero_coords(players_hero[id_hero].y_hero,
                                                              players_hero[id_hero].x_hero + 1)
                        if not (e.mod == pygame.KMOD_LSHIFT):
                            cam_y, cam_x = (i * tile_size - ii // 2 for i, ii in
                                            zip(players_hero[id_hero].give_hero_coords(), res[::-1]))

            for button in buttons:
                button.handle_event(e)
            if e.type == pygame.USEREVENT:
                if e.button == buttons[0]:
                    print('0')
                elif e.button == buttons[1]:
                    flag_player = not flag_player
                    cam_y, cam_x = (i * tile_size - ii // 2 for i, ii in
                                    zip(players_hero[::-1][id_hero].give_hero_coords(), res[::-1]))
                    steps_current_hero = players_hero[::-1][id_hero].give_hero_steps()
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
            chunks[i].render()

        for button in buttons:
            button.check_hover([int(i * (res[n] / size[n])) for n, i in enumerate(pygame.mouse.get_pos())])
            button.draw(screen)
        window.blit(pygame.transform.scale(screen, size), (0, 0))
        screen.blit(pygame.transform.scale(window, size), (0, 0))
        pygame.display.update()
        clock.tick(480)

        frame += 1
        if frame % 4 == 0:
            if flag_player:
                hero1_animated.update()
            else:
                hero2_animated.update()

        if frame % 100 == 0:
            pygame.display.set_caption('FPS: ' + str(round(clock.get_fps())))
            chunks_on_screen((cam_x, cam_y), chunk_size, tile_size, res, (world_size_chunk_x, world_size_chunk_y))
    return ret


def castle_draw(user_id, can_add_new_building, hero_in_castle=False):
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


switch_scene(castle_draw(2, True))
# switch_scene(game_world_draw)
data_game = 'data/maps/map_1.txt'
while current_scene is not None:
    data_game = current_scene(data_game)
pygame.quit()
