from menu_start import Menu, BasicMenu
from func_load_image import load_image
import pygame  # импорт библиотеки PyGame
from PIL import Image

pygame.init()  # инициализируем PyGame

WIDTH = 1920  # ширина экрана
HEIGHT = 1080  # высота экрана

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)  # создаем поверхность экрана

current_scene = None
image = "zamok_gorod_fentezi_174584_1920x1080.jpg"


def switch_scene(scene):
    global current_scene
    current_scene = scene


def setting_screen():
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
                if e.key == pygame.K_w:
                    menu.switch(-1)
                elif e.key == pygame.K_s:
                    menu.switch(1)
                elif e.key == pygame.K_SPACE:
                    menu.select()
                    running = False
        screen.blit(load_image(image), (0, 0))
        menu.draw(screen, 800, 400, 75)
        pygame.display.flip()


def basic_menu_draw():
    # global screen
    # size = 1920, 1080
    # screen = pygame.display.set_mode(size)
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
                if e.key == pygame.K_w:
                    menu.switch(-1)
                elif e.key == pygame.K_s:
                    menu.switch(1)
                elif e.key == pygame.K_SPACE:
                    menu.select()
                    running = False
        screen.blit(load_image(image), (0, 0))
        menu.draw(screen, 800, 400, 75)
        pygame.display.flip()


def menu_draw():
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
                if e.key == pygame.K_w:
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
    img_objects_map = {'A': [load_image('data/imgs/hero.png')],
                       'B': [load_image('data/imgs/abstract-blue-painting-acrylic-texture-with-marble-pattern.jpg')],
                       '#': [load_image('data/imgs/kust.png')],
                       '-': [load_image(
                           'data/imgs/1626746394_9-kartinkin-com-p-pikselnaya-tekstura-travi-krasivo-11.jpg')],
                       '*': [load_image('data/imgs/')],
                       '@': [load_image('data/imgs/go_zamok.png')],
                       '$': [load_image('data/imgs/go_zamok.png')],
                       'G': [load_image('data/imgs/1677316897_foni-club-p-sunduk-piksel-art-1.png')],
                       'W': [load_image('data/imgs/—Pngtree—wood log lumber pile cartoon_6955308.png')],
                       'R': [load_image('data/imgs/')],
                       'M': [load_image('data/imgs/kristal.jpg')],
                       'O': [load_image('data/imgs/image0000.jpg')],
                       'K': [load_image('data/imgs/b94adf7c5d21d13a83be3878336d0378.jpg')],
                       'I': [load_image('data/imgs/')],
                       'F': [load_image('data/imgs/gadalka.jpg')],
                       '1': [load_image('data/imgs/as.jpg')],
                       '2': [load_image('data/imgs/34174417_2210_w032_n002_608b_p15_608.jpg')],
                       '3': [load_image('data/imgs/molot.jpg')],
                       '4': [load_image('data/imgs/')],
                       '5': [load_image('data/imgs/70015845_JEMA GER 1640-02.jpg')]
                       }
    size = [800, 800]
    res = [400, 400]

    cam_x, cam_y = 0, 0
    global screen
    screen = pygame.display.set_mode(size)
    window = pygame.transform.scale(screen, res)

    clock = pygame.time.Clock()

    chunk_size = 8
    tile_size = 16

    textures = {0: [pygame.image.load('0.png')],
                1: [pygame.image.load('1.png')]}

    world_size_chunk_x = 1024 // chunk_size
    world_size_chunk_y = 1024 // chunk_size

    world_map = Image.open('world.png').load()

    def chunks_on_screen(cam, chunk_size, tile_size, res, world_size_chunk):
        x1 = cam[0] // (chunk_size * tile_size)
        y1 = cam[1] // (chunk_size * tile_size)

        x2 = (cam[0] + res[0]) // (chunk_size * tile_size)
        y2 = (cam[1] + res[1]) // (chunk_size * tile_size)

        x1 = min(max(x1, 0), world_size_chunk[0] - 1)
        x2 = min(max(x2, 0), world_size_chunk[1] - 1)

        y1 = min(max(y1, 0), world_size_chunk[0] - 1)
        y2 = min(max(y2, 0), world_size_chunk[1] - 1)

        result = []
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                result.append(x + y * world_size_chunk[0])

        return result

    def generate_tile(x, y, chunk_x, chunk_y, w_map):
        tile_x = (chunk_x // tile_size) + x
        tile_y = (chunk_y // tile_size) + y

        return int(x % 2 == 0)

    class Chunk:
        def __init__(self, x, y, w_map):
            self.x, self.y = x, y
            self.map = [generate_tile(x, y, self.x, self.y, w_map) for y in range(chunk_size) for x in
                        range(chunk_size)]

        def render(self):
            for y in range(chunk_size):
                for x in range(chunk_size):
                    texture = textures[self.map[x + y * chunk_size]][0]
                    screen.blit(texture, (self.x + x * tile_size - cam_x, self.y + y * tile_size - cam_y))

    running = True
    chunks = []
    for y in range(world_size_chunk_y):
        for x in range(world_size_chunk_x):
            chunks.append(Chunk(x * chunk_size * tile_size, y * chunk_size * tile_size, world_map))

    frame = 0
    while running:
        screen.fill((0, 0, 0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_q:
                    switch_scene(menu_draw)
                    running = False

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            cam_x -= 1
        if key[pygame.K_d]:
            cam_x += 1
        if key[pygame.K_w]:
            cam_y -= 1
        if key[pygame.K_s]:
            cam_y += 1

        for i in chunks_on_screen((cam_x, cam_y), chunk_size, tile_size, res, (world_size_chunk_x, world_size_chunk_y)):
            chunks[i].render()

        window.blit(pygame.transform.scale(screen, size), (0, 0))
        pygame.display.update()
        clock.tick(480)

        frame += 1
        if frame % 100 == 0:
            pygame.display.set_caption('FPS: ' + str(round(clock.get_fps())))
            chunks_on_screen((cam_x, cam_y), chunk_size, tile_size, res, (world_size_chunk_x, world_size_chunk_y))

    switch_scene(basic_menu_draw)
    while current_scene is not None:
        current_scene()
    pygame.quit()
