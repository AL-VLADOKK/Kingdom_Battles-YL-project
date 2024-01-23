import pygame
from func_load_image import load_image


def chunks_on_screen(cam, chunk_size, tile_size, res, world_size_chunk):
    x1 = cam[0] // (chunk_size * tile_size)
    y1 = cam[1] // (chunk_size * tile_size)

    x2 = (cam[0] + res[0]) // (chunk_size * tile_size)
    y2 = (cam[1] + res[1]) // (chunk_size * tile_size)

    x1 = min(max(x1, 0), world_size_chunk[0] - 1)
    x2 = min(max(x2, 0), world_size_chunk[0] - 1)

    y1 = min(max(y1, 0), world_size_chunk[1] - 1)
    y2 = min(max(y2, 0), world_size_chunk[1] - 1)

    result = []
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            result.append(x + y * world_size_chunk[1])

    return result


def resources_on_screen(screen, resources, steps, x, y, width, height, scroll, sps_resources_img):
    texture = pygame.transform.scale(scroll, (width, height))
    resurs_n = list(resources) + [steps]
    for i in range(len(sps_resources_img)):
        texture.blit(sps_resources_img[i], (width * i // 5, 2 * height // 10))
        texture.blit(pygame.font.SysFont('arial', 15).render(str(resurs_n[i]), True, (255, 255, 255)), (int(width * i // 5 + width * 1 // 10), 2 * height // 10))
    screen.blit(texture, (x, y))
    return screen
