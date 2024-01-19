def create_fog_war(map, chr_h):
    fog = [[True for _ in range(len(map[0]))] for __ in range(len((map)))]
    return change_fog_war(map, fog, chr_h)


def change_fog_war(map, fog, chr_h):
    fog_r = fog
    for i in range(len(map)):
        for ii in range(len(map[0])):
            if chr_h in map[i][ii]:
                fog_r[i - 3:i + 4] = [[False if ii - 3 <= r <= ii + 3 else fog_r[i + rr][r] for r in range(len(map[0]))] for rr in range(-3, 4)]
                return fog_r
