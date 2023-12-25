import copy


def map_symbol(current: [int], prev: [int], symbol: str) -> [int]:
    result = current
    match symbol:
        case "|":
            if current[0] < prev[0]:
                result[0] -= 1
            else:
                result[0] += 1
        case "-":
            if current[1] < prev[1]:
                result[1] -= 1
            else:
                result[1] += 1
        case "J":
            if current[1] == prev[1]:
                result[1] -= 1
            else:
                result[0] -= 1
        case "F":
            if current[1] == prev[1]:
                result[1] += 1
            else:
                result[0] += 1
        case "L":
            if current[1] == prev[1]:
                result[1] += 1
            else:
                result[0] -= 1
        case "7":
            if current[1] == prev[1]:
                result[1] -= 1
            else:
                result[0] += 1
        case _:
            print("Error: ", symbol)
            return

    return result


def get_length(start: [int], next_step: [int], field: [str]) -> int:
    counter = 1
    current = next_step  # [52, 101]
    prev = start  # [52, 100]
    while current != start:
        symbol = field[current[0]][current[1]]
        copy_current = copy.deepcopy(current)
        next_field = map_symbol(current, prev, symbol)
        prev = copy_current
        counter += 1

    return counter


if __name__ == "__main__":
    with open("pipe_input.txt", "r") as f:
        field = f.readlines()

    print(field[52][100])
    start = [52, 100]
    next_step = [52, 101]

    loop_length = get_length(start, next_step, field)

    print("Result Part 1: ", loop_length / 2)
