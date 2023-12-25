
import copy


def get_map(instructions):
    current = [0, 0]
    coords = [copy.deepcopy(current)]
    filled_cords = []
    last_instruction = ""
    turn_right = 0
    turn_left = 0

    for instruction in instructions:
        if instruction[0] == "R":
            if last_instruction == "U":
                turn_right += 1
            if last_instruction == "D":
                turn_left += 1
            last_instruction = "R"
            for i in range(instruction[1]):
                coords.append(copy.deepcopy(current))
                filled_cords.append([current[0] + 1, current[1]])
                current[1] += 1
        if instruction[0] == "L":
            if last_instruction == "D":
                turn_right += 1
            if last_instruction == "U":
                turn_left += 1
            last_instruction = "L"
            for i in range(instruction[1]):
                coords.append(copy.deepcopy(current))
                filled_cords.append([current[0] - 1, current[1]])
                current[1] -= 1
        if instruction[0] == "D":
            if last_instruction == "R":
                turn_right += 1
            if last_instruction == "L":
                turn_left += 1
            last_instruction = "D"
            for i in range(instruction[1]):
                coords.append(copy.deepcopy(current))
                filled_cords.append([current[0], current[1] - 1])
                current[0] += 1
        if instruction[0] == "U":
            if last_instruction == "L":
                turn_right += 1
            if last_instruction == "R":
                turn_left += 1
            last_instruction = "U"
            for i in range(instruction[1]):
                coords.append(copy.deepcopy(current))
                filled_cords.append([current[0], current[1] + 1])
                current[0] -= 1
    left, right, up, down = 0, 0, 0, 0
    print("turns [L, R]: ", turn_left, turn_right)
    for coord in coords:
        if coord[0] < up:
            up = coord[0]
        if coord[0] > down:
            down = coord[0]
        if coord[1] < left:
            left = coord[1]
        if coord[1] > right:
            right = coord[1]

    new_coords = []
    new_filled = []
    for coord in coords:
        new_coords.append([coord[0] + abs(up), coord[1] + abs(left)])
    for coord in filled_cords:
        new_filled.append([coord[0] + abs(up), coord[1] + abs(left)])
    return new_coords, new_filled, down - up, right - left


def count_hashes(list_to_print):
    result = 0
    for line in list_to_print:
        for letter in line:
            if letter == "#":
                result += 1
    return result


def count_os(list_to_print):
    result = 0
    for line in list_to_print:
        for letter in line:
            if letter == "O":
                result += 1
    return result


def update_os(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == ".":
                positions = []
                for m in [-1, 1]:
                    for n in [-1, 1]:
                        if i + m >= 0 and j + n >= 0:
                            positions.append([i+m, j+n])

                o_counter = 0
                for pos in positions:
                    try:
                        if field[pos[0]][pos[1]] == "O":
                            o_counter += 1
                    except:
                        continue
                if o_counter >= 1:
                    field[i][j] = "O"


def fill_os(field):
    result = copy.deepcopy(field)
    start_count = count_os(result)
    update_os(result)
    new_count = count_os(result)
    while new_count > start_count:
        start_count = copy.deepcopy(new_count)
        update_os(result)
        new_count = count_os(result)

    return result


def print_map(coords, filled, length, width):
    list_to_print = []
    for i in range(length + 1):
        line = []
        for j in range(width + 1):
            line.append(".")
        list_to_print.append(line)
    for coord in coords:
        list_to_print[coord[0]][coord[1]] = "#"
    for coord in filled:
        try:
            if list_to_print[coord[0]][coord[1]] != "#":
                list_to_print[coord[0]][coord[1]] = "O"
        except:
            continue
    new = fill_os(list_to_print)
    return new


def part1(instructions):
    coords, filled, length, width = get_map(instructions)
    new = print_map(coords, filled, length, width)
    return count_hashes(new) + count_os(new)


if __name__ == "__main__":
    with open("day18_input.txt", "r") as f:
        lines = f.readlines()

    instructions = []
    for line in lines:
        a = line.split()
        instructions.append((a[0], int(a[1])))

    solution_part1 = part1(instructions)
    print("Solution Part 1: ", solution_part1)
