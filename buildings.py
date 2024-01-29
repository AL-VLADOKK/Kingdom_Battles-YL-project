import pygame
from reading_map import map_reading
import sqlite3
import os


class Buildings:
    def __init__(self, map):
        self.building = {}
        list_map = map_reading(map)
        for i_index, i in enumerate(list_map):
            for j_index, j in enumerate(i):
                if j == 'O' or j == 'K' or j == 'I' or j == 'F':
                    coords = (j_index, i_index)
                    self.building[coords] = ['yes', j]
        db = "GameDB.db3"
        db = os.path.join('data/db', db)
        self.con = sqlite3.connect(db)


def usage(self, coords, turn):
    if coords not in self.building.keys():
        pass
    elif self.building[coords][0] == 'no':
        pass
    elif self.building[coords][0] == 'yes':
        cur = self.con.cursor()
        if self.building[coords][1] == 'O':
            building = 5
        elif self.building[coords][1] == 'K':
            building = 6
        elif self.building[coords][1] == 'I':
            building = 7
        elif self.building[coords][1] == 'F':
            building = 8
        building_result = cur.execute("""SELECT resources, traits, resource_value, trait_value
              FROM buildings WHERE id = ?""", (building,)).fetchone()

        resource = building_result[0]
        if resource == 1:
            resource = 'gold'
        if resource == 2:
            resource = 'wood'
        if resource == 3:
            resource = 'rock'
        if resource == 4:
            resource = 'magic_crystal'

        trait = building_result[1]
        resource_value = building_result[2]
        trait_value = building_result[3]
        if turn == 'A':
            user = 2
        elif turn == 'B':
            user = 3
        if resource is not None:
            user_result = cur.execute(f"""SELECT {resource} FROM user_resources 
                  WHERE id = ?""", (user,)).fetchone()
            new_resource_value = int(user_result[0]) + int(resource_value)
            cur.execute(f"""UPDATE user_resources SET {resource} = ? WHERE id = ?""",
                        (new_resource_value, user,))
        if trait is not None:
            trait = cur.execute("""SELECT name FROM traits 
                  WHERE id = ?""", (trait,)).fetchone()
            trait_result = cur.execute(f"""SELECT {trait} FROM traits 
                  WHERE id = ?""", (trait, user,)).fetchone()
            new_trait_value = int(trait_result[0]) + int(trait_value)
            cur.execute(f"""UPDATE traits SET {trait} = ? WHERE id = ?""",
                        (new_trait_value, user,))
        self.con.commit()
        cur.close()
        self.building[coords] = ['no', self.building[coords][1]]


class RedCastle:
    def __init__(self):
        self.building = {}
        db = "GameDB.db3"
        db = os.path.join('data/db', db)
        self.con = sqlite3.connect(db)
        self.list_l = ['lvl', 'horse_stable', 'marketplace', 'militia', 'pennies', 'swordmans', 'knights', 'archer',
                       'crossbowman', 'cleric', 'abbot', 'master_of_light_and_might', 'horseman']
        self.buying_army = {}
        self.load_data()

    def load_data(self):
        cur = self.con.cursor()
        result = cur.execute("""SELECT lvl, horse_stable, marketplace, militia, pennies, swordmans, knights, archer, 
        crossbowman, cleric, abbot, master_of_light_and_might, horseman FROM castles WHERE id = 2""").fetchone()
        for i in range(len(self.list_l)):
            self.building[self.list_l[i]] = result[i]
        for i in range(10):
            buying_army = cur.execute("""SELECT unit_name FROM units WHERE id = ?""",
                                      (i + 1,)).fetchone()
            buying_army_result = cur.execute(f"""SELECT {buying_army[0]} FROM army WHERE id = 7""").fetchone()
            self.buying_army[buying_army[0]] = buying_army_result[0]

    def update_castle(self):
        if self.building['lvl'] <= 2:
            cur = self.con.cursor()
            price = cur.execute("""SELECT gold, wood, rock, magic_cristalls FROM castle_units WHERE id = ?""",
                                (12 + self.building['lvl'],)).fetchone()
            resources = cur.execute("""SELECT gold, wood, rock, magic_crystal FROM user_resources 
            WHERE id = 2""").fetchone()
            if resources[0] >= price[0] and resources[1] >= price[1] and resources[2] >= price[2] and (
                    resources[3] >= price[3]):
                cur.execute("""UPDATE user_resources SET gold = ? WHERE id = 2""",
                            (resources[0] - price[0],))
                cur.execute("""UPDATE user_resources SET wood = ? WHERE id = 2""",
                            (resources[1] - price[1],))
                cur.execute("""UPDATE user_resources SET rock = ? WHERE id = 2""",
                            (resources[2] - price[2],))
                cur.execute("""UPDATE user_resources SET magic_crystal = ? WHERE id = 2""",
                            (resources[3] - price[3],))
                cur.execute("""UPDATE castles SET lvl = ? WHERE id = 2""",
                            (self.building['lvl'] + 1,))
            self.con.commit()
            cur.close()
            self.load_data()

    def new_building(self, building):
        if self.building[building] == 'no':
            cur = self.con.cursor()
            price = cur.execute("""SELECT gold, wood, rock, magic_cristalls FROM castle_units WHERE id = ?""",
                                (list(self.building.keys()).index(building),)).fetchone()
            resources = cur.execute("""SELECT gold, wood, rock, magic_crystal FROM user_resources 
                        WHERE id = 2""").fetchone()
            if resources[0] >= price[0] and resources[1] >= price[1] and resources[2] >= price[2] and (
                    resources[3] >= price[3]):
                cur.execute("""UPDATE user_resources SET gold = ? WHERE id = 2""",
                            (resources[0] - price[0],))
                cur.execute("""UPDATE user_resources SET wood = ? WHERE id = 2""",
                            (resources[1] - price[1],))
                cur.execute("""UPDATE user_resources SET rock = ? WHERE id = 2""",
                            (resources[2] - price[2],))
                cur.execute("""UPDATE user_resources SET magic_crystal = ? WHERE id = 2""",
                            (resources[3] - price[3],))
                cur.execute(f"""UPDATE castles SET {building} = ? WHERE id = 2""", ('yes',))
            self.con.commit()
            cur.close()
            self.load_data()

    def add_buying_army(self):
        cur = self.con.cursor()
        for i in range(10):
            if self.list_l[i + 3] == 'yes':
                unit_name = cur.execute("""SELECT unit_name FROM units WHERE id = ?""",
                                        (i + 1,)).fetchone()
                weekly_addition = cur.execute("""SELECT value FROM castle_units WHERE id = ?""",
                                              (i + 3,)).fetchone()
                self.buying_army[unit_name[0]] += weekly_addition[0]
                cur.execute(f"""UPDATE army SET {unit_name[0]} = ? WHERE id = 7""",
                            (self.buying_army[unit_name[0]],))
        self.con.commit()
        cur.close()
        self.load_data()

    def buy_army(self, unit):
        if self.buying_army[unit] > 0:
            cur = self.con.cursor()
            gold = cur.execute("""SELECT gold FROM user_resources WHERE id = 2""").fetchone()
            price = cur.execute("""SELECT price FROM units WHERE unit_name = ?""",
                                (unit,)).fetchone()
            if gold[0] >= price[0]:
                self.buying_army[unit] -= 1
                castle_army = cur.execute(f"""SELECT {unit} FROM army WHERE id = 4""").fetchone()
                cur.execute(f"""UPDATE army SET {unit} = ? WHERE id = 7""",
                            (self.buying_army[unit],))
                cur.execute(f"""UPDATE army SET {unit} = ? WHERE id = 4""",
                            (castle_army[0] + 1,))
                cur.execute("""UPDATE user_resources SET gold = ? WHERE id = 2""",
                            (gold[0] - price[0],))
            self.con.commit()
            cur.close()
            self.load_data()

    def add_army_to_hero(self, unit):
        cur = self.con.cursor()
        castle_army = cur.execute(f"""SELECT {unit} FROM army WHERE id = 4""").fetchone()
        if castle_army[0] > 0:
            result_check = cur.execute(f"""SELECT * FROM army WHERE id = 3""").fetchone()
            n = 0
            for i in range(2, 12):
                if result_check[i] != 0:
                    n += 1
            if n <= 6:
                user_army = cur.execute(f"""SELECT {unit} FROM army WHERE id = 3""").fetchone()
                cur.execute(f"""UPDATE army SET {unit} = ? WHERE id = 3""",
                            (user_army[0] + 1,))
                cur.execute(f"""UPDATE army SET {unit} = ? WHERE id = 4""",
                            (castle_army[0] - 1,))
                self.con.commit()
                cur.close()
                self.load_data()

    def add_gold(self):
        if self.building['marketplace'] == 'yes':
            cur = self.con.cursor()
            gold = cur.execute("""SELECT gold FROM user_resources WHERE id = 2""").fetchone()
            new_gold = gold[0] + 1000
            cur.execute("""UPDATE user_resources SET gold = ? WHERE id = 2""", (new_gold,))
            self.con.commit()
            cur.close()


class BlueCastle:
    def __init__(self):
        self.building = {}
        db = "GameDB.db3"
        db = os.path.join('data/db', db)
        self.con = sqlite3.connect(db)
        self.list_l = ['lvl', 'horse_stable', 'marketplace', 'militia', 'pennies', 'swordmans', 'knights', 'archer',
                       'crossbowman', 'cleric', 'abbot', 'master_of_light_and_might', 'horseman']
        self.buying_army = {}
        self.load_data()

    def load_data(self):
        cur = self.con.cursor()
        result = cur.execute("""SELECT lvl, horse_stable, marketplace, militia, pennies, swordmans, knights, archer, 
        crossbowman, cleric, abbot, master_of_light_and_might, horseman FROM castles WHERE id = 3""").fetchone()
        for i in range(len(self.list_l)):
            self.building[self.list_l[i]] = result[i]
        for i in range(10):
            buying_army = cur.execute("""SELECT unit_name FROM units WHERE id = ?""",
                                      (i + 1,)).fetchone()
            buying_army_result = cur.execute(f"""SELECT {buying_army[0]} FROM army WHERE id = 8""").fetchone()
            self.buying_army[buying_army[0]] = buying_army_result[0]

    def update_castle(self):
        if self.building[0] <= 2:
            cur = self.con.cursor()
            price = cur.execute("""SELECT gold, wood, rock, magic_cristalls FROM castle_units WHERE id = ?""",
                                (12 + self.building[0],)).fetchone()
            resources = cur.execute("""SELECT gold, wood, rock, magic_crystal FROM user_resources 
            WHERE id = 3""").fetchone()
            if resources[0] >= price[0] and resources[1] >= price[1] and resources[2] >= price[2] and (
                    resources[3] >= price[3]):
                cur.execute("""UPDATE user_resources SET gold = ? WHERE id = 3""",
                            (resources[0] - price[0],))
                cur.execute("""UPDATE user_resources SET wood = ? WHERE id = 3""",
                            (resources[1] - price[1],))
                cur.execute("""UPDATE user_resources SET rock = ? WHERE id = 3""",
                            (resources[2] - price[2],))
                cur.execute("""UPDATE user_resources SET magic_crystal = ? WHERE id = 3""",
                            (resources[3] - price[3],))
                cur.execute("""UPDATE castles SET lvl = ? WHERE id = 3""",
                            (self.building[0] + 1,))
            self.con.commit()
            cur.close()
            self.load_data()

    def new_building(self, building):
        if self.building[building] == 'no':
            cur = self.con.cursor()
            price = cur.execute("""SELECT gold, wood, rock, magic_cristalls FROM castle_units WHERE id = ?""",
                                (list(self.building.keys()).index(building),)).fetchone()
            resources = cur.execute("""SELECT gold, wood, rock, magic_crystal FROM user_resources 
                        WHERE id = 3""").fetchone()
            if resources[0] >= price[0] and resources[1] >= price[1] and resources[2] >= price[2] and (
                    resources[3] >= price[3]):
                cur.execute("""UPDATE user_resources SET gold = ? WHERE id = 3""",
                            (resources[0] - price[0],))
                cur.execute("""UPDATE user_resources SET wood = ? WHERE id = 3""",
                            (resources[1] - price[1],))
                cur.execute("""UPDATE user_resources SET rock = ? WHERE id = 3""",
                            (resources[2] - price[2],))
                cur.execute("""UPDATE user_resources SET magic_crystal = ? WHERE id = 3""",
                            (resources[3] - price[3],))
                cur.execute(f"""UPDATE castles SET {building} = ? WHERE id = 3""", ('yes',))
            self.con.commit()
            cur.close()
            self.load_data()

    def add_buying_army(self):
        cur = self.con.cursor()
        for i in range(10):
            if self.list_l[i + 3] == 'yes':
                unit_name = cur.execute("""SELECT unit_name FROM units WHERE id = ?""",
                                        (i + 1,)).fetchone()
                weekly_addition = cur.execute("""SELECT value FROM castle_units WHERE id = ?""",
                                              (i + 3,)).fetchone()
                self.buying_army[unit_name[0]] += weekly_addition[0]
                cur.execute(f"""UPDATE army SET {unit_name[0]} = ? WHERE id = 8""",
                            (self.buying_army[unit_name[0]],))
        self.con.commit()
        cur.close()
        self.load_data()

    def buy_army(self, unit):
        if self.buying_army[unit] > 0:
            cur = self.con.cursor()
            gold = cur.execute("""SELECT gold FROM user_resources WHERE id = 3""").fetchone()
            price = cur.execute("""SELECT price FROM units WHERE unit_name = ?""",
                                (unit,)).fetchone()
            if gold[0] >= price[0]:
                self.buying_army[unit] -= 1
                castle_army = cur.execute(f"""SELECT {unit} FROM army WHERE id = 6""").fetchone()
                cur.execute(f"""UPDATE army SET {unit} = ? WHERE id = 8""",
                            (self.buying_army[unit],))
                cur.execute(f"""UPDATE army SET {unit} = ? WHERE id = 6""",
                            (castle_army[0] + 1,))
                cur.execute("""UPDATE user_resources SET gold = ? WHERE id = 3""",
                            (gold[0] - price[0],))
            self.con.commit()
            cur.close()
            self.load_data()

    def add_army_to_hero(self, unit):
        cur = self.con.cursor()
        castle_army = cur.execute(f"""SELECT {unit} FROM army WHERE id = 6""").fetchone()
        if castle_army[0] > 0:
            result_check = cur.execute(f"""SELECT * FROM army WHERE id = 4""").fetchone()
            n = 0
            for i in range(2, 12):
                if result_check[0][i] != 0:
                    n += 1
            if n <= 6:
                user_army = cur.execute(f"""SELECT {unit} FROM army WHERE id = 5""").fetchone()
                cur.execute(f"""UPDATE army SET {unit} = ? WHERE id = 5""",
                            (user_army[0] + 1,))
                cur.execute(f"""UPDATE army SET {unit} = ? WHERE id = 6""",
                            (castle_army[0] - 1,))
                self.con.commit()
                cur.close()
                self.load_data()

    def add_gold(self):
        if self.building['marketplace'] == 'yes':
            cur = self.con.cursor()
            gold = cur.execute("""SELECT gold FROM user_resources WHERE id = 3""").fetchone()
            new_gold = gold[0] + 1000
            cur.execute("""UPDATE user_resources SET gold = ? WHERE id = 3""", (new_gold,))
            self.con.commit()
            cur.close()

