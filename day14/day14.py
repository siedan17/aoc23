import copy
import time
from functools import lru_cache


def turn_field(field):
    new_field = copy.deepcopy(field)
    for i in range(len(new_field)):
        for j in range(len(new_field[0])):
            if new_field[i][j] == "O":
                new_index = i
                for k in range(1, i+1):
                    if new_field[i - k][j] not in ["O", "#"] and new_field[i - k][j] == ".":
                        new_index -= 1
                    if new_field[i - k][j] != "." or i - k == 0:
                        if new_index == i:
                            break
                        new_field[new_index][j] = "O"
                        new_field[i][j] = "."
                        break

    return new_field


def count_of_stones(field):
    result = 0
    height = len(field)
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == "O":
                result += (height - i)
    return result


def print_field(field):
    for line in field:
        new_line = ""
        for letter in line:
            new_line += letter
        print(new_line)


def number_os(field):
    result = 0
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == "O":
                result += 1
    return result


# def part1(field):
#     new_field = turn_field(field)
#     # print_field(field)
#     # print("----")
#     # print_field(new_field)
#     # print("----")
#     # print(number_os(new_field))
#     return count_of_stones(new_field)

def rotate_field(field):
    result_field = []
    for i in range(len(field)):
        new_line = []
        for j in range(len(field[0])):
            new_line.append(field[len(field) - 1 - j][i])
        result_field.append(new_line)
    return result_field


@lru_cache
def cycle(field_input):
    field = list(list(inner_list) for inner_list in field_input)
    result_field = copy.deepcopy(field)
    north_tilted = turn_field(result_field)
    rotated = rotate_field(north_tilted)
    west_tilted = turn_field(rotated)
    rotated = rotate_field(west_tilted)
    south_tilted = turn_field(rotated)
    rotated = rotate_field(south_tilted)
    east_tilted = turn_field(rotated)
    rotated = rotate_field(east_tilted)
    return rotated


def part2(field):
    result = count_of_stones(field)
    field_to_try = field
    results = []
    times = []
    for i in range(1000):
        start = time.time()
        input_tuple = tuple(tuple(inner_list) for inner_list in field_to_try)
        new_field = cycle(input_tuple)
        # print_field(new_field)
        # print("---")
        new_result = count_of_stones(new_field)
        if new_result != result:
            result = new_result
        field_to_try = new_field
        results.append(result)
        end = time.time()
        times.append(end - start)
    print(results)
    # print(times[-10:])
    return result


off = [99136, 99130, 99175, 99230, 99253, 99254, 99220, 99148, 99064, 98963, 98871, 98790, 98735, 98689, 98597, 98494, 98392, 98289, 98187, 98083, 97984, 97877, 97813, 97747, 97670, 97607, 97540, 97496, 97430, 97383, 97325, 97272, 97247, 97204, 97154, 97147, 97088, 97035, 96992, 96957, 96914, 96886, 96836, 96775, 96751, 96685, 96611, 96544, 96464, 96399, 96364, 96330, 96319, 96311, 96279, 96271,
       96252, 96208, 96154, 96098, 96034, 95970, 95925, 95872, 95828, 95804, 95767, 95737, 95721, 95688, 95676, 95673, 95649, 95658, 95656, 95654, 95679, 95710, 95730, 95766, 95809, 95836, 95866, 95897, 95898, 95921, 95973, 95997, 96015, 96052, 96058, 96062, 96069, 96064, 96060, 96066, 96026, 95989, 95977, 95933, 95892, 95864, 95819, 95786, 95778, 95750, 95741, 95744, 95736, 95748, 95769, 95783, 95821]
period = [95868, 95879, 95899, 95930, 95963, 95998, 96024, 96042, 96059, 96071, 96059, 96065, 96069, 96056, 96027, 95998, 95967, 95934, 95901, 95854, 95820, 95795, 95768, 95751, 95750, 95734, 95737, 95757, 95759, 95784, 95830, 95858, 95880, 95908, 95920, 95964, 96007, 96014, 96043, 96068, 96061, 96060, 96074, 96059, 96057, 96036,
          95988, 95968, 95943, 95891, 95855, 95829, 95785, 95769, 95760, 95740, 95735, 95746, 95747, 95760, 95793, 95820, 95859, 95889, 95898, 95921, 95973, 95997, 96015, 96052, 96058, 96062, 96069, 96064, 96060, 96066, 96026, 95989, 95977, 95933, 95892, 95864, 95819, 95786, 95778, 95750, 95741, 95744, 95736, 95748, 95769, 95783, 95821]


def do():
    a = 1000000000
    a = a - len(off)
    b = a % len(period)
    return period[b - 1]


if __name__ == "__main__":
    with open("day14_input.txt", "r") as f:
        lines = f.readlines()

    field = []
    for line in lines:
        row = []
        for i in range(len(line)-1):
            row.append(line[i])
        field.append(row)

    # solution_part1 = part1(field)

    # print("Solution Part 1: ", solution_part1)

    # solution_part2 = part2(field)
    solution_part2 = do()
    print("Solution Part2: ", solution_part2)
