
import copy


def get_coords(field):
    current = [0, 0]
    result = [current]
    perimeter = 0

    for turn in field:
        if turn[1] == 0:
            current[1] += turn[0]
            result.append(copy.deepcopy(current))
        if turn[1] == 1:
            current[0] += turn[0]
            result.append(copy.deepcopy(current))
        if turn[1] == 2:
            current[1] -= turn[0]
            result.append(copy.deepcopy(current))
        if turn[1] == 3:
            current[0] -= turn[0]
            result.append(copy.deepcopy(current))
        perimeter += turn[0]

    return result, perimeter


def shoelace(coords):
    result = 0
    for i in range(len(coords)):
        if i < len(coords) - 1:
            result += coords[i][0] * coords[i + 1][1]
            result -= coords[i][1] * coords[i + 1][0]
        else:
            result += coords[i][0] * coords[0][1]
            result -= coords[i][1] * coords[0][0]

    return abs(result) / 2


def part2(field):
    coords, perimeter = get_coords(field)
    area = shoelace(coords)
    print(area)
    """
    I am interested in num of interior points and points on the perimeter.
    Pick's Theorem: A = I + p/2 - 1 I...interior; A...Area enclosed; p...points on perimeter
    Shoelace gives formular for Area. (irregular as well)
    """
    result = area + perimeter / 2 + 1
    return result


if __name__ == "__main__":
    with open("day18_input.txt", "r") as f:
        lines = f.readlines()

    instructions = []
    for line in lines:
        a = line.split()[2][1:-1]
        instructions.append((int(a[:-1][1:], 16), int(a[-1])))

    solution_part2 = part2(instructions)
    print("Solution Part 2: ", solution_part2)
