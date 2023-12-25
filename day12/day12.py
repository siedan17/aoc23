
from functools import lru_cache
import copy

def get_first(field):
    for i in range(len(field)):
        if field[i] == "#":
            return i
    return -1


def get_last(field):
    for i in range(len(field)):
        if field[-1 - i] == "#":
            return len(field) - 1 - i
    return 0


def clean_field(field):
    result = []
    for i in field:
        if i != ".":
            result.append(i)
    return result

@lru_cache(maxsize=None)
def get_count(field: (str), numbers: (int)) -> int:
    count = 0
    num = numbers[0]
    for i in range(len(field)):
        if num > len(clean_field(field[i:])):
            continue
        if field[i] == ".":
            continue
        if len(numbers) == 1:
            if i + num < get_last(field):
                continue
        if i > get_first(field) and get_first(field) != -1:
            continue
        if field[i] in ["#", "?"]:
            trial = field[i:i+num]
            if "." in trial:
                continue
            if len(field) > i + num and field[i+num] == "#":
                continue
            if len(numbers) > 1:
                count += get_count(field[i + num + 1:], numbers[1:])
            else:
                count += 1

    return count


if __name__ == "__main__":
    with open("day12_input.txt", "r") as f:
        lines = f.readlines()

    input_dict = []

    for line in lines:
        a = line.split()
        c = a[1].split(",")
        d = [int(i) for i in c]
        field = a[0]
        y = copy.deepcopy(d)
        for i in range(4):
            y += d
            field += "?" + a[0]
        field += "."
        x = [i for i in field]
        input_dict.append((tuple(x), tuple(y)))

    sum = 0
    for e in input_dict:
        sum += get_count(e[0], e[1])

    print("Solution Part 1: ", sum)