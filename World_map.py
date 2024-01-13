import pygame
from func_load_image import load_image


def chunks_on_screen(cam, chunk_size, tile_size, res, world_size_chunk):
    x1 = cam[0] // (chunk_size * tile_size)
    y1 = cam[1] // (chunk_size * tile_size)

    x2 = (cam[0] + res[0]) // (chunk_size * tile_size)
    y2 = (cam[1] + res[1]) // (chunk_size * tile_size)

    x1 = min(max(x1, 0), world_size_chunk[0] - 1)
    x2 = min(max(x2, 0), world_size_chunk[1] - 1)

    y1 = min(max(y1, 0), world_size_chunk[0] - 1)
    y2 = min(max(y2, 0), world_size_chunk[1] - 1)

    result = []
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            result.append(x + y * world_size_chunk[0])

    return result
