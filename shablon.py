import pygame, os, sqlite3
import random
from units_class import Unit


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
    a = random.randint(min, sum - min + 1)
    b = sum - a
    return a, b


class Hero:
    coast_lvl_up_exp = [100, 300, 600, 1000, 1500, 2200, 3300, 5000, 7000, 10000]
    sum_give_characteristics = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4]
    d_give_characteristics = {0: lambda: random_two_nubers(1, 0) + (0, 0),
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
        self.slots_army = []
        self.visited_buildings = []
        self.aurs_stable_hors = 0
        self.x_hero = 0
        self.y_hero = 0

        db = "GameDB.db3"
        db = os.path.join('data/db', db)
        self.con = sqlite3.connect(db)

        cur = self.con.cursor()
        result = cur.execute("""SELECT * FROM heroes WHERE id = ?""", (self.id,)).fetchone()
        hor = cur.execute("""SELECT horse_stable FROM castles WHERE id = ?""", (self.id,)).fetchone()
        if hor[0] == 'yes':
            self.aurs_stable_hors = 7
        self.name = result[1]
        self.chr = 'A' if self.name == 'red_hero' else 'B'
        self.steps = result[2]
        self.attack = result[3]
        self.protection = result[4]
        self.inspiration = result[5]
        self.luck = result[6]
        self.slot_1 = result[7]
        self.slot_2 = result[8]
        self.slot_3 = result[9]
        self.slot_4 = result[10]

        resurs = cur.execute("""SELECT gold, wood, rock, magic_crystal from user_resources WHERE id = ?""",
                             (self.id,)).fetchone()

        self.gold = resurs[0]
        self.wood = resurs[1]
        self.rock = resurs[2]
        self.cristal = resurs[3]

        id_arm = 3 if self.id == 2 else 5
        arms = cur.execute("""SELECT peasant, penny, swordman, knight, archer,
                crossbowman, cleric, abbot, horseman, master_of_light_and_might from army WHERE id = ?""",
                           (id_arm,)).fetchone()

        for i in range(len(arms)):
            if len(self.slots_army) > 5:
                pass
            else:
                if arms[i] != 0:
                    self.slots_army.append([Unit(Unit.r_d[Unit.id_in_d[i]]), arms[i]])
        for i in range(6 - len(self.slots_army)):
            self.slots_army.append(False)

    def load_db(self):
        cur = self.con.cursor()
        cur.execute("""UPDATE heroes SET motion = ?, damage = ?, protection = ?, inspiration = ?, luck = ?,
                slot_a = ?, slot_b = ?, slot_c = ?, slot_d = ? WHERE id = ?""",
                    (self.steps, self.attack, self.protection, self.inspiration, self.luck, self.slot_1,
                     self.slot_2, self.slot_3, self.slot_4, self.id))
        self.con.commit()
        cur.execute("""UPDATE user_resources SET gold = ?, wood = ?, rock = ?, magic_crystal = ? WHERE id = ?""",
                    (self.gold, self.wood, self.rock, self.cristal, self.id))
        self.con.commit()
        hor = cur.execute("""SELECT horse_stable FROM castles WHERE id = ?""", (self.id,)).fetchone()
        if hor[0] == 'yes':
            self.aurs_stable_hors = 7
        arm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in self.slots_army:
            if type(i) != bool:
                arm[i[0].d_in_id[i[0].name]] = i[1]

        id_arm = 3 if self.id == 2 else 5
        cur.execute("""UPDATE army SET peasant = ?, penny = ?, swordman = ?, knight = ?, archer = ?,
                crossbowman = ?, cleric = ?, abbot = ?, horseman = ?, master_of_light_and_might = ? WHERE id = ?""",
                    (arm[0], arm[1], arm[2], arm[3], arm[4], arm[5],
                     arm[6], arm[7], arm[8], arm[9], id_arm))
        self.con.commit()
        cur.close()

    def give_characteristics(self):
        return [self.attack, self.protection, self.luck, self.inspiration]

    def add_artefats(self, chr_artefact):
        cur = self.con.cursor()
        result = cur.execute("""SELECT name, trait, value FROM artifacts""").fetchall()
        if chr_artefact == '3':  # молот
            if not self.slot_2:
                self.slot_2 = result[2]
                self.luck += result[2][2]
        elif chr_artefact == '4':  # скрижаль
            if not self.slot_3:
                self.slot_3 = result[3]
                self.luck += result[3][2]
        elif chr_artefact == '5':  # клевер
            if not self.slot_4:
                self.slot_4 = result[4]
                self.luck += result[4][2]
        elif chr_artefact == '1':  # свиток урона
            if self.slot_1 == 'Свиток урона':
                pass
            elif self.slot_1 == 'Свиток защиты':
                self.slot_1 = result[0]
                self.attack += result[0][2]
                self.protection -= result[1][2]
            else:
                self.slot_1 = result[0]
                self.attack += result[0][2]
        elif chr_artefact == '2':  # свиток защиты
            if self.slot_1 == 'Свиток урона':
                self.slot_1 = result[1]
                self.attack -= result[0][2]
                self.protection += result[1][2]
            elif self.slot_1 == 'Свиток защиты':
                pass
            else:
                self.slot_1 = result[1]
                self.protection += result[1][2]

    def add_visited_building(self, tile_y, tile_x):
        self.visited_buildings.append((tile_y, tile_x))

    def give_visited_buildings(self):
        return self.visited_buildings

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
        a, p, i, l = Hero.d_give_characteristics[self.level]()
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

    def give_hero_steps(self):
        steps = int(self.steps * 1.5) if self.aurs_stable_hors else self.steps
        self.aurs_stable_hors = max(0, self.aurs_stable_hors - 1)
        return steps

    def visited_the_stables(self):
        self.aurs_stable_hors = 7

    def give_resources(self):
        return self.gold, self.wood, self.rock, self.cristal
