import pygame
from func_load_image import load_image


class Menu:

    # 2й вариант меню
    def __init__(self):
        self.option_surface = []  # список поверхностей(список будущих пунктов меню)
        self.defs = []  # список функций для пунктов
        self.index = 0  # индекс выбранного пункта
        self.coords_options_surface = []

    def append_option(self, option, deff):  # добавить пункт
        self.option_surface.append(pygame.font.SysFont('arial', 44).render(option, True, (255, 255, 255)))
        self.defs.append(deff)

    def switch(self, direction):  # перемещение по меню
        # конструкция против выхода индекса за рамки меню
        self.index = max(0, min(self.index + direction, len(self.option_surface) - 1))

    def select(self):  # вызов функции
        self.defs[self.index]()

    def draw(self, surf, x, y, padding):
        for i, option in enumerate(self.option_surface):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * padding)
            self.coords_options_surface.append(option_rect)
            if i == self.index:
                pygame.draw.rect(surf, (0, 0, 100), option_rect)
            surf.blit(option, option_rect)

    def click(self, coords):
        for option_rect in self.coords_options_surface:
            if option_rect.collidepoint(coords):
                self.index = self.coords_options_surface.index(option_rect)
                self.select()
                break


class BasicMenu(Menu):
    link_image = 'scroll.png'

    def draw(self, surf, x, y, padding):
        image = load_image(BasicMenu.link_image)
        image = pygame.transform.scale(image, (400, 200 + len(self.option_surface) * padding))
        rect = image.get_rect()
        rect = rect.move((x - 80, y - 90))
        surf.blit(image, rect)
        super().draw(surf, x, y, padding)
