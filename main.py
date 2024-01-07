import pygame


class Menu:
    def __init__(self):
        pass

    def click(self, x, y):
        pass


import pygame  # импорт библиотеки PyGame

pygame.init()  # инициализируем PyGame

WIDTH = 1920  # ширина экрана
HEIGHT = 1080  # высота экрана

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создаем поверхность экрана

# running = True
# while running:
#     for e in pygame.event.get():  # перебираем события
#         if e.type == pygame.QUIT:  # если тип события выход из игры, то
#             running = False
#
#     # код для обновления и отрисовки здесь
#
#     pygame.display.flip()  # обновляем экран
#
# pygame.quit()

current_scene = None


def switch_scene(scene):
    global current_scene
    current_scene = scene

def scene1():
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN:
                switch_scene(scene2)
                running = False
        screen.fill((255, 0, 0))
        pygame.display.flip()


def scene2():
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN:
                switch_scene(scene1)
                running = False
        screen.fill((0, 255, 0))
        pygame.display.flip()


switch_scene(scene1)
while current_scene is not None:
    current_scene()
pygame.quit()
