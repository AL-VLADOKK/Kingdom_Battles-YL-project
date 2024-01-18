import os


def map_reading(map):
    map = os.path.join('data/maps', map)
    f = open(map, encoding="utf8")
    map_list = f.read().replace('\t', '').split('\n')
    return map_list
