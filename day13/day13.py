
import numpy as np
import copy


def get_horizontal(pattern: [[int]], check_input: [int, str], from_vert: False) -> [int, str]:
    result = 0
    list_of_results = []
    check = [-1, ""]
    if not from_vert and check_input[1] == "horizontal":
        check = check_input
    if from_vert and check_input[1] == "vertical":
        check = check_input

    for m in range(1, len(pattern)):
        looking_left = 0
        looking_right = 2 * m
        if m > int((len(pattern) - 1) / 2):
            looking_left = m - (len(pattern) - m)
            looking_right = len(pattern)
        up = pattern[looking_left:m]
        down = pattern[m:looking_right]
        up.reverse()
        if up == down:
            if m != check[0]:
                list_of_results.append(m)
    if len(list_of_results) > 0:
        result = max(list_of_results)
    
    return [result, "horizontal"]


def get_vertical(pattern: [[int]], check: [int, str]) -> [int, str]:
    new_pattern = np.array(pattern).T.tolist()
    return [get_horizontal(new_pattern, check, True)[0], "vertical"]

def perform(pattern: [[int]], check: [int, str]) -> [int, str]:
    result = 0
    result_str = ""
    horizontal = get_horizontal(pattern, check, False)
    vertical = get_vertical(pattern, check)
    if horizontal[0] > 0:
        result += 100 * horizontal[0]
        result_str = "horizontal"
    else:
        result += vertical[0]
        result_str = "vertical"

    small_result = 0
    if result_str == "horizontal":
        small_result = horizontal[0]
    else:
        small_result = vertical[0]

    return [result, [small_result, result_str]]

def wrapper_part_two(pattern: [[int]]) -> int:
    old_pattern = copy.deepcopy(pattern)
    old_result = perform(old_pattern, [-1, ""])[0]
    old_orient = perform(old_pattern, [-1, ""])[1]
    result = 0
    list_of_previous = [result]

    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            new_pattern = copy.deepcopy(pattern)
            if new_pattern != old_pattern:
                print('error')
            if new_pattern[i][j] == 0:
                new_pattern[i][j] = 1
            else:
                new_pattern[i][j] = 0
            new_result = perform(new_pattern, old_orient)[0]
            if new_result not in list_of_previous:
                list_of_previous.append(new_result)
                result = new_result

    if len(list_of_previous) > 2:
        if list_of_previous.index(old_result) == 2:
            result = list_of_previous[1]

    return result




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


    part2 = 0

    for pattern in list_of_patterns:
        part2 += wrapper_part_two(pattern)

    print("Solution Part 2: ", part2)
