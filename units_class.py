import pygame, os, sqlite3


class Unit:
    d = {'k': 'peasant',
         'K': 'penny',
         's': 'swordman',
         'S': 'knight',
         'a': 'archer',
         'A': 'crossbowman',
         'c': 'cleric',
         'C': 'abbot',
         'H': 'horseman',
         'M': 'master_of_light_and_might'}

    r_d = {}
    for k, v in d.items():
        if k != 'M':
            r_d[v] = k
        else:
            r_d['angel'] = k

    d_in_id = {'peasant': 0,
               'penny': 1,
               'swordman': 2,
               'knight': 3,
               'archer': 4,
               'crossbowman': 5,
               'cleric': 6,
               'abbot': 7,
               'horseman': 8,
               'master_of_light_and_might': 9}

    id_in_d = {}
    for k, v in d_in_id.items():
        if k != 'master_of_light_and_might':
            id_in_d[v] = k
        else:
            id_in_d[v] = 'angel'

    def __init__(self, chr):
        db = "GameDB.db3"
        db = os.path.join('data/db', db)
        self.con = sqlite3.connect(db)

        self.name = Unit.d[chr]
        cur = self.con.cursor()

        result = cur.execute("""SELECT * FROM units WHERE unit_name = ?""", (self.name,)).fetchone()

        self.motion = result[2]
        self.initiative = result[3]
        self.health_points = result[4]
        self.damage = result[5]
        self.protection = result[6]
        self.inspiration = result[7]
        self.luck = result[8]

    def scroll(self, damage, protection, inspiration, luck):
        point_one = (self.damage + damage + self.protection + protection) * (
                3 - 2 // self.initiative) * self.health_points
        point_one = int(point_one * (1 + (self.luck + luck) // 10) if self.luck + luck else point_one)
        point_one = int(point_one * (1 + (self.inspiration + inspiration) // 10) if self.luck + luck else point_one)
        return point_one

    def point_to_health(self, damage, protection, inspiration, luck):
        point_one = (self.damage + damage + self.protection + protection) * (
                3 - 2 // self.initiative) * self.health_points
        point_one = int(point_one * (1 + (self.luck + luck) // 10) if self.luck + luck else point_one)
        point_one = int(point_one * (1 + (self.inspiration + inspiration) // 10) if self.luck + luck else point_one)
        return point_one * 2
