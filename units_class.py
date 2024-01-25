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
         'M': 'master of light and might'}

    def __init__(self, chr):
        self.name = str(Unit.d[chr])  # нужно подключить бд
        self.initiative = 1
        self.health_points = 1
        self.damage = 1
        self.protection = 1
        self.inspiration = 0
        self.luck = 0

    def scroll(self, damage, protection, inspiration, luck):
        point_one = (self.damage + damage + self.protection + protection) * (
                3 - 2 // self.initiative) * self.health_points
        point_one = point_one * (1 + (self.luck + luck) // 10) if self.luck + luck else point_one
        point_one = int(point_one * (1 + (self.inspiration + inspiration) // 10) if self.luck + luck else point_one)
        return point_one

    def point_to_health(self, damage, protection, inspiration, luck, points):
        points = points / (1 + (self.inspiration + inspiration) // 10) if self.luck + luck else points
        points = points / (1 + (self.luck + luck) // 10) if self.luck + luck else points
        health = points / (self.damage + damage + self.protection + protection) * (
                3 - 2 // self.initiative)
        return int(health)
