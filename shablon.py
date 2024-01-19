import pygame, os, sqlite3
import random


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


def random_two_nubers(sum, min):
    a = random.randint(min, sum - min)
    b = sum - a
    return (a, b)


class Hero:
    coast_lvl_up_exp = [10, 30, 60, 100, 150, 220, 330, 500, 700, 1000]
    sum_give_characteristics = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4]
    give_characteristics = {0: lambda: random_two_nubers(1, 0) + (0, 0),
                            1: lambda: random_two_nubers(1, 0) + (0, 0),
                            2: lambda: random_two_nubers(1, 0) + (0, 0),
                            3: lambda: random_two_nubers(2, 0) + (0, 0),
                            4: lambda: random_two_nubers(2, 0) + random_two_nubers(1, 0),
                            5: lambda: random_two_nubers(3, 1) + (0, 0),
                            6: lambda: random_two_nubers(3, 1) + (0, 0),
                            7: lambda: random_two_nubers(3, 1) + (0, 0),
                            8: lambda: random_two_nubers(3, 1) + (0, 0),
                            9: lambda: random_two_nubers(4, 1) + random_two_nubers(2, 0)}

    def __init__(self, *args):
        self.number, self.id = args
        self.level, self.exp = 0, 0
        self.slots_army = [None, None, None, None, None, None]
        self.aurs_stable_hors = 0
        self.construction = []  # сюда будут сохранятся ссылки на обьекты на карте или их кординаты, которые посещаются один раз(кузня, оружейник)
        self.x_hero = 0
        self.y_hero = 0

        db = "GameDB.db3"
        db = os.path.join('data/db', db)
        self.con = sqlite3.connect(db)

        cur = self.con.cursor()
        result = cur.execute("""SELECT * FROM heroes WHERE id = ?""", (self.id,)).fetchone()
        self.name = result[1]
        self.chr = 'A' if self.name == 'red_hero' else 'B'
        self.motion = result[2]
        self.attack = result[3]
        self.protection = result[4]
        self.inspiration = result[5]
        self.luck = result[6]
        self.slot_1 = result[7]
        self.slot_2 = result[8]
        self.slot_3 = result[9]
        self.slot_4 = result[10]

    def give_exp(self, exp):
        self.exp += exp
        if self.exp >= Hero.coast_lvl_up_exp[self.level]:
            if self.level < 9:
                self.exp = 0
                self.level += 1
                self.level_up()
            else:
                self.exp = Hero.coast_lvl_up_exp[9]

    def level_up(self):
        a, p, i, l = Hero.give_characteristics[self.level]
        self.attack += a
        self.protection += p
        self.inspiration += i
        self.luck += l

    def find_hero_coords(self, map):
        for i in range(len(map)):
            for ii in range(len(map[0])):
                if map[i][ii] == self.chr:
                    self.x_hero, self.y_hero = ii, i

    def give_hero_coords(self):
        return self.y_hero, self.x_hero

    def set_hero_coords(self, y, x):
        self.x_hero, self.y_hero = x, y

    link_on_hero_1_animation = ['', '', '', '', '']
    link_on_hero_2_animation = ['', '', '', '', '']
