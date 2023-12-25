import copy
from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)


@lru_cache
def update_map(map, coord, input):
    result = list(map)
    for i in range(len(result)):
        if i == coord[0]:
            new_line = [x for x in result[i]]
            new_line[coord[1]] = input
            result[i] = tuple(new_line)
            break
    return tuple(result)


@lru_cache
def get_possible(map, coord):
    if map[coord[0]][coord[1]] == "<":
        return tuple([(coord[0], coord[1] - 1)])
    if map[coord[0]][coord[1]] == ">":
        return tuple([(coord[0], coord[1] + 1)])
    if map[coord[0]][coord[1]] == "^":
        return tuple([(coord[0] - 1, coord[1])])
    if map[coord[0]][coord[1]] == "v":
        return tuple([(coord[0] + 1, coord[1])])
    result = []
    for i in [-1, 1]:
        trial = [coord[0] + i, coord[1]]
        if map[trial[0]][trial[1]] in ".<>v^":
            result.append(tuple(trial))
    for j in [-1, 1]:
        trial = [coord[0], coord[1] + j]
        if map[trial[0]][trial[1]] in ".<>v^":
            result.append(tuple(trial))
    return tuple(result)


def print_map(map):
    for line in map:
        string_line = ""
        for letter in line:
            string_line += letter
        print(string_line)
    print("---------------------------------------")


@lru_cache
def count_os(map):
    result = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "O":
                result += 1
    return result


def count_rocks(map):
    result = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "#":
                result += 1
    return result


absolute_best = 0


@lru_cache
def part1(map, coord, last):
    if coord[0] == len(map) - 1:  # ending case
        global absolute_best
        count_of_os = count_os(map)
        if count_of_os > absolute_best:
            absolute_best = count_of_os
            print("## " + str(absolute_best) + " ##")
            print_map(map)
        return 1

    options = get_possible(map, coord)
    map = update_map(map, coord, "O")
    for option in options:
        if option != last:
            part1(map, option, coord)


if __name__ == "__main__":
    with open("day23_input.txt", "r") as f:
        lines = f.readlines()

    map = []
    for line in lines:
        line = line.strip()
        map.append(tuple([symbol for symbol in line]))

    map = update_map(tuple(map), (0, 1), "O")
    # print(count_rocks(map))

    part1(tuple(map), (1, 1), (0, 1))
    print("Solution Part 1: ", absolute_best)
