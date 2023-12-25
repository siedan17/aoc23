
import numpy as np


def get_horizontal(pattern: [[int]]) -> int:
    result = 0
    list_of_results = []
    for m in range(1, len(pattern)):
        looking_left = 0
        looking_right = 2 * m
        if m > int((len(pattern) - 1) / 2):
            looking_left = m - (len(pattern) - m)
            looking_right = len(pattern)
        up = pattern[looking_left:m]
        down = pattern[m:looking_right]
        # print(up, "--", down)
        up.reverse()
        if up == down:
            # print(up)
            # print(down)
            list_of_results.append(m)
    if len(list_of_results) > 0:
        result = max(list_of_results)
    return result


def get_vertical(pattern: [[int]]) -> int:
    new_pattern = np.array(pattern).T.tolist()
    # print(pattern, "--- \n", new_pattern)
    return get_horizontal(new_pattern)


if __name__ == "__main__":
    with open("day13_input.txt", "r") as f:
        lines = f.readlines()

    list_of_patterns = []
    new_pattern = []
    for j in range(len(lines)):
        new_pattern.append([0 if i == "." else 1 for i in lines[j][:-1]])
        if lines[j] == '\n':
            list_of_patterns.append(new_pattern)
            new_pattern = []
        if j + 1 == len(lines):
            new_pattern.append([])
            list_of_patterns.append(new_pattern)

    for line in list_of_patterns:
        line.pop()

    # print(len(list_of_patterns[-1][0]))

    part1 = 0

    for pattern in list_of_patterns:
        print(pattern)
        horizontal = get_horizontal(pattern)
        # horizontal = 0
        if horizontal > 0:
            part1 += 100 * horizontal
        else:
            vertical = get_vertical(pattern)
            part1 += vertical

    print("Solution Part 1: ", part1)

    # part2 = 0

    # print("Solution Part 2: ", part2)
