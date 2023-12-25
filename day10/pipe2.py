import copy


def map_symbol(current: [int], prev: [int], symbol: str) -> [[int]]:
    result = []
    c_current = copy.deepcopy(current)
    turn = ""
    match symbol:
        case "|":
            if current[0] < prev[0]:
                result.append([c_current[0],  # take right side!
                               c_current[1] + 1])
                current[0] -= 1
            else:
                result.append([c_current[0],
                               c_current[1] - 1])
                current[0] += 1
        case "-":
            if current[1] < prev[1]:
                result.append([c_current[0] - 1,
                               c_current[1]])
                current[1] -= 1
            else:
                result.append([c_current[0] + 1,
                               c_current[1]])
                current[1] += 1
        case "J":
            if current[1] == prev[1]:
                current[1] -= 1
                turn = "right"
            else:
                current[0] -= 1
                turn = "left"
                result.append([c_current[0] + 1,
                               c_current[1]])
                result.append([c_current[0] + 1,
                               c_current[1] + 1])
                result.append([c_current[0],
                               c_current[1] + 1])
        case "F":
            if current[1] == prev[1]:
                current[1] += 1
                turn = "right"
            else:
                current[0] += 1
                turn = "left"
                result.append([c_current[0] - 1,
                               c_current[1]])
                result.append([c_current[0] - 1,
                               c_current[1] - 1])
                result.append([c_current[0],
                               c_current[1] - 1])
        case "L":
            if current[1] == prev[1]:
                current[1] += 1
                turn = "left"
                result.append([c_current[0] + 1,
                               c_current[1]])
                result.append([c_current[0] + 1,
                               c_current[1] - 1])
                result.append([c_current[0],
                               c_current[1] - 1])
            else:
                current[0] -= 1
                turn = "right"
        case "7":
            if current[1] == prev[1]:
                current[1] -= 1
                turn = "left"
                result.append([c_current[0] - 1,
                               c_current[1]])
                result.append([c_current[0] - 1,
                               c_current[1] + 1])
                result.append([c_current[0],
                               c_current[1] + 1])
            else:
                current[0] += 1
                turn = "right"
        case _:
            print("Error: ", symbol)
            return
    return result


def update_os(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == "_":
                positions = []
                for m in [-1, 1]:
                    for n in [-1, 1]:
                        if 140 > i + m >= 0 and 140 > j + n >= 0:
                            positions.append([i+m, j+n])
                o_counter = 0
                for pos in positions:
                    if field[pos[0]][pos[1]] == "O":
                        o_counter += 1
                if o_counter >= 2:
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


def count_os(field):
    counter = 0
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == "O":
                counter += 1
    return counter


def get_length(start: [int], next_step: [int], field: [str]) -> int:
    counter = 1
    new_field = copy.deepcopy(field)
    current = next_step  # [52, 101]
    prev = start  # [52, 100]
    # right = 0
    # left = 0
    while current != start:
        symbol = field[current[0]][current[1]]
        copy_current = copy.deepcopy(current)
        new_field[current[0]][current[1]] = 'X'
        inside_fields = map_symbol(
            current, prev, symbol)  # updates current!
        # if c_turn == "right":
        #     right += 1
        # if c_turn == "left":
        #     left += 1
        for inside_field in inside_fields:
            if new_field[inside_field[0]][inside_field[1]] != 'X':
                new_field[inside_field[0]][inside_field[1]] = 'O'

        new_field[current[0]][current[1]] = 'X'
        prev = copy_current
        counter += 1

    # print(right, left)  # 4371, 4367
    for i in range(len(new_field)):
        for j in range(len(new_field[0])):
            if new_field[i][j] not in ["X", "O"]:
                new_field[i][j] = "_"
    return counter, new_field


if __name__ == "__main__":
    with open("pipe_input.txt", "r") as f:
        lines = f.readlines()

    start = [52, 100]
    next_step = [52, 101]

    field = []
    for i in range(140):
        field.append([])
        for j in range(140):
            field[i].append(lines[i][j])

    loop_length, updated_field = get_length(start, next_step, field)

    filled_field = fill_os(updated_field)

    count = count_os(filled_field)
    print(count)

    # print_field = []
    # for l in filled_field:
    #     string_line = ""
    #     for letter in l:
    #         string_line += letter
    #     print_field.append(string_line)

    # for l in print_field:
    #     print(l)
