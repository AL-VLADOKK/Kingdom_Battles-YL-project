import pygame


class Menu:
    def __init__(self):
        pass

    def click(self, x, y):
        pass


font = pygame.font.SysFont('arial', 50)


class Menu_2:  # 2й вариант меню
    def __init__(self, ):
        self.option_surface = []  # список поверхностей(список будущих пунктов меню)
        self.defs = []  # список функций для пунктов
        self.index = 0  # индекс выбранного пункта

    def append_option(self, option, deff):  # добавить пункт
        self.option_surface.append(font.render(option, True, (255, 255, 255)))
        self.defs.append(deff)

    def switch(self, direction):  # перемещение по меню
        # конструкция против выхода индекса за рамки меню
        self.index = max(0, min(self.index + direction, len(self.option_surface) - 1))

    def select(self):  # вызов функции
        self.defs[self.index]()
