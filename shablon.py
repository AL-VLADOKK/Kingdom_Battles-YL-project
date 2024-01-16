import pygame
import random
from PIL import Image
from func_load_image import load_image

pygame.init()

size = [800, 800]
res = [400, 400]

cam_x, cam_y = 0, 0

window = pygame.display.set_mode(size)
screen = pygame.transform.scale(window, res)

clock = pygame.time.Clock()

chunk_size = 8
tile_size = 16

textures = {0: [pygame.image.load('data/imgs/abstract-blue-painting-acrylic-texture-with-marble-pattern.jpg')],
            1: [pygame.image.load('data/imgs/1626746394_9-kartinkin-com-p-pikselnaya-tekstura-travi-krasivo-11.jpg')]}

world_size_chunk_x = 1024 // chunk_size
world_size_chunk_y = 1024 // chunk_size

world_map = Image.open('data/imgs/world.png').load()


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


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__()
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Hero:
    def __init__(self, *args):
        self.link_on_hero_animation, self.number, characteristics = args
        self.name, self.motion, self.attack, self.protection, self.inspiration, self.luck, self.slot_1, self.slot_2, self.slot_3, self.slot_4 = characteristics
        self.slots_army = [None, None, None, None, None, None]
        self.slots_artefacts = [None, None, None, None]
        self.aurs_stable_hors = False
        self.construction = []  # сюда будут сохранятся ссылки на обьекты на карте или их кординаты, которые посещаются один раз(кузня, оружейник)
        self.course = (1, 1)  # направление героя (для тайлов) 1-1 вверх, 0-0 вниз 1-0 влево 0-1 вправо
        self.sprite = AnimatedSprite(load_image("dragon_sheet8x2.png"), 8, 2, 50, 50)

    def construction_add(self, coords_cell):
        self.construction = self.construction + [coords_cell]


class World:
    dict_objects_map = {'A': Hero,
                        'B': Hero,
                        '#': None,
                        '-': None,
                        '*': None,
                        '@': None,
                        '$': None,
                        'G': None,
                        'W': None,
                        'R': None,
                        'M': None,
                        'O': None,
                        'K': None,
                        'I': None,
                        'F': None,
                        '1': None,
                        '2': None,
                        '3': None,
                        '4': None,
                        '5': None
                        }
    link_on_hero_1_animation = ['', '', '', '', '']
    link_on_hero_2_animation = ['', '', '', '', '']

    def __init__(self, link_map, hero_0, hero_1):
        self.map = [i.split() for i in open(f'{link_map}', mode="r").read().split('/n')]
        self.hero_1, self.hero_2 = Hero(World.link_on_hero_1_animation, 'A', hero_0), Hero(
            World.link_on_hero_2_animation, 'B', hero_1)

        self.world = [
            [World.dict_objects_map[ii]() if ii != 'A' or ii != 'B' else self.hero_1 if ii == 'A' else self.hero_2 for ii
             in i] for i in self.map]


class Chunk:
    def __init__(self, x, y, w_map):
        self.x, self.y = x, y
        self.map = [generate_tile(x, y, self.x, self.y, w_map) for y in range(chunk_size) for x in range(chunk_size)]

    def render(self):
        for y in range(chunk_size):
            for x in range(chunk_size):
                texture = textures[self.map[x + y * chunk_size]][0]
                screen.blit(texture, (self.x + x * tile_size - cam_x, self.y + y * tile_size - cam_y))


chunks = []
for y in range(world_size_chunk_y):
    for x in range(world_size_chunk_x):
        chunks.append(Chunk(x * chunk_size * tile_size, y * chunk_size * tile_size, world_map))

frame = 0
while 1:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

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
