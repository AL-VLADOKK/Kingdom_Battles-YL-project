import pygame
from func_load_image import load_image

class Menu:
    def __init__(self):
        pass

    def click(self, x, y):
        pass

link_image = 'scroll.png'
class Menu_2:
    # 2й вариант меню
    def __init__(self, ):
        self.option_surface = []  # список поверхностей(список будущих пунктов меню)
        self.defs = []  # список функций для пунктов
        self.index = 0  # индекс выбранного пункта

    def append_option(self, option, deff):  # добавить пункт
        self.option_surface.append(pygame.font.SysFont('arial', 50).render(option, True, (255, 255, 255)))
        self.defs.append(deff)

    def switch(self, direction):  # перемещение по меню
        # конструкция против выхода индекса за рамки меню
        self.index = max(0, min(self.index + direction, len(self.option_surface) - 1))

    def select(self):  # вызов функции
        self.defs[self.index]()

    def draw(self, surf, x, y, padding):
        image = load_image(link_image)
        image = pygame.transform.scale(image, (350, 200 + len(self.option_surface) * padding))
        rect = image.get_rect()
        rect = rect.move((x - 80, y - 90))
        surf.blit(image, rect)
        for i, option in enumerate(self.option_surface):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * padding)
            if i == self.index:
                pygame.draw.rect(surf, (0, 0, 100), option_rect)
            surf.blit(option, option_rect)
