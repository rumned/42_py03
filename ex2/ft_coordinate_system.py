#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    coor_tuple: tuple[float, float, float] | None = None
    while coor_tuple is None:
        player_pos: str = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        passed_args = player_pos.split(',')
        if len(passed_args) != 3:
            print("3 coordinates in float format is needed")
            continue
        try:
            x, y, z = tuple(float(i) for i in passed_args)
            coor_tuple = (x, y, z)
        except Exception as e:
            print(e)
            continue
    print(f"Inputted coordinate : {coor_tuple}")
    print(f"X={coor_tuple[0]}, Y={coor_tuple[1]}, Z={coor_tuple[2]}")
    return coor_tuple


def calculate_distance(
        c_1: tuple[float, float, float],
        c_2: tuple[float, float, float] | None = None) -> float:
    if c_2 is None:
        c_2 = (0, 0, 0)
        is_2nd_coor = False
    else:
        is_2nd_coor = True
    dist: float = math.sqrt(((c_1[0] - c_2[0]) ** 2) +
                            ((c_1[1] - c_2[1]) ** 2) +
                            ((c_1[2] - c_2[2]) ** 2))
    if is_2nd_coor:
        print("Distance between the 2 sets of coordinates: "
              f"{round(dist, 4)}")
    else:
        print(f"Distance from center: {round(dist, 4)}")
    return dist


if __name__ == '__main__':
    print('== Game Coordinate System ==\n')
    print('Get a first set of coordinates')
    pos_1 = get_player_pos()
    calculate_distance(pos_1)
    print()
    print('Get a first set of coordinates')
    pos_2 = get_player_pos()
    calculate_distance(pos_1, pos_2)
