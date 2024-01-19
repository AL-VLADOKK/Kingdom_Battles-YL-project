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


switch_scene(game_world_draw)
data_game = 'data/maps/map_1.txt'
while current_scene is not None:
    data_game = current_scene(data_game)
pygame.quit()
