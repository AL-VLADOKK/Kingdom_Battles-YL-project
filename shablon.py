import pygame
from func_load_image import load_image


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
        self.sprite_stand = AnimatedSprite(load_image("dragon_sheet8x2.png", colorkey=-1), 1, 3, 50, 50)
        self.sprite_stand = AnimatedSprite(load_image("dragon_sheet8x2.png", colorkey=-1), 1, 4, 50, 50)

    def construction_add(self, coords_cell):
        self.construction = self.construction + [coords_cell]

    link_on_hero_1_animation = ['', '', '', '', '']
    link_on_hero_2_animation = ['', '', '', '', '']
