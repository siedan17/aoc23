
import copy


def get_hash(string):
    current_value = 0
    for letter in string:
        ascii_code = ord(letter)
        current_value += ascii_code
        current_value *= 17
        current_value = current_value % 256
    return current_value


# def part1(strings):
#     result = 0
#     for string in strings:
#         result += get_hash(string)
#     return result

def get_map():
    result = {}
    for i in range(256):
        result[i] = []
    return result


def update_map(current_map, string):
    new_map = copy.deepcopy(current_map)
    if "-" in string:
        label = string.split("-")[0]
        hash_of_label = get_hash(label)
        lookup_list = copy.deepcopy(current_map[hash_of_label])
        for i in range(len(lookup_list)):
            if lookup_list[i][0] == label:
                del lookup_list[i]
                new_map[hash_of_label] = lookup_list
                break
        return new_map
    
    if "=" in string:
        label = string.split("=")[0]
        hash_of_label = get_hash(label)
        lookup_list = copy.deepcopy(current_map[hash_of_label])
        len_of_lens = int(string.split("=")[1])
        lookup_list = copy.deepcopy(current_map[hash_of_label])
        seen = False
        for i in range(len(lookup_list)):
            if lookup_list[i][0] == label:
                lookup_list[i][1] = len_of_lens
                new_map[hash_of_label] = lookup_list
                seen = True
                break
        if not seen:
            lookup_list.append([label, len_of_lens])
            new_map[hash_of_label] = lookup_list
        return new_map

    print("here -> error?")
    return new_map


def part2(strings):
    empty_map = get_map()
    current_map = empty_map
    for string in strings:
        current_map = update_map(current_map, string)

    # print(current_map)
    result = 0
    for key in current_map.keys():
        for i in range(len(current_map[key])):
            result += (key+1) * (i+1) * current_map[key][i][1]

    return result


if __name__ == "__main__":
    with open("day15_input.txt", "r") as f:
        lines = f.readlines()
        # print(len(lines))

    a = lines[0].split(',')

    # solution_part1 = part1(a)

    # print("Solution Part 1: ", solution_part1)

    solution_part2 = part2(a)

    print("Solution Part2: ", solution_part2)
