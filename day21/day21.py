
import copy


def get_num(map):
    result = 0
    counter = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "O":
                result += 1
    return result


def print_map(map):
    print_list = []
    for line in map:
        new_string = ""
        for letter in line:
            new_string += letter
        print_list.append(new_string)
    for line in print_list:
        print(line)


def update(map):
    new_os = []
    old_os = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "O" or map[i][j] == "S":
                old_os.append((i, j))
                new_points = []
                for r_num in [-1, 1]:
                    new_points.append((i+r_num, j))
                for c_num in [-1, 1]:
                    new_points.append((i, j+c_num))
                for point in new_points:
                    if 0 <= point[0] < len(map) and 0 <= point[1] < len(map[0]):
                        if map[point[0]][point[1]] != "#":
                            new_os.append(point)

    for point in old_os:
        map[point[0]][point[1]] = "."

    for point in new_os:
        map[point[0]][point[1]] = "O"


def part1(map):
    map = copy.deepcopy(map)
    for _ in range(327):
        update(map)
    # print_map(map)
    count = get_num(map)
    return count


if __name__ == "__main__":
    with open("day21_input.txt", "r") as f:
        lines = f.readlines()

    map = []
    for line in lines + lines + lines + lines + lines:
        line = line.strip()
        new_line = []
        for letter in line + line + line + line + line:
            new_line.append(letter)
        map.append(new_line)

    # print(len(map), len(map[0]))
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "S" and not (i == 327 and j == 327):
                map[i][j] = "."

    solution_part1 = part1(map)
    print("Solution Part 1: ", solution_part1)
