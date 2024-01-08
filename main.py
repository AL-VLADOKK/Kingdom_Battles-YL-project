import pygame
from menu_start import Menu
from func_load_image import load_image
import pygame  # импорт библиотеки PyGame

pygame.init()  # инициализируем PyGame

WIDTH = 1920  # ширина экрана
HEIGHT = 1080  # высота экрана

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создаем поверхность экрана

current_scene = None
image = "zamok_gorod_fentezi_174584_1920x1080.jpg"


def switch_scene(scene):
    global current_scene
    current_scene = scene


def menu_draw():
    menu = Menu()
    menu.append_option('Hello world', lambda: print('Hello world'))
    menu.append_option('закрытие', quit)
    menu.append_option(' world', lambda: print(' world'))
    running = True
    screen.blit(load_image(image), (10, 10))
    menu.draw(screen, 800, 400, 75)
    while running:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                menu.click(e.pos)
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_q:
                    switch_scene(scene2)
                    running = False
                elif e.key == pygame.K_w:
                    menu.switch(-1)
                elif e.key == pygame.K_s:
                    menu.switch(1)
                elif e.key == pygame.K_SPACE:
                    menu.select()
        screen.blit(load_image(image), (10, 10))
        menu.draw(screen, 800, 400, 75)
        pygame.display.flip()


def scene2():
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_q:
                    switch_scene(menu_draw)
                    running = False
        screen.fill((0, 255, 0))
        pygame.display.flip()


switch_scene(menu_draw)
while current_scene is not None:
    current_scene()
pygame.quit()
