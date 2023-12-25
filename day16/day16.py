
import sys

sys.setrecursionlimit(10**6)

seen = []


def get_coords(field: [[str]], direction: str, start_point: (int)) -> [(int)]:
    if (direction, start_point) in seen:
        return []
    seen.append((direction, start_point))
    if start_point[0] < 0 or start_point[0] > 109:
        return []
    if start_point[1] < 0 or start_point[1] > 109:
        return []
    result = [start_point]
    if direction == "right":
        if field[start_point[0]][start_point[1]] in [".", "-"]:
            new_points = get_coords(
                field, "right", (start_point[0], start_point[1] + 1))
        if field[start_point[0]][start_point[1]] == "|":
            new_points = get_coords(
                field, "up", (start_point[0] - 1, start_point[1])) + get_coords(
                field, "down", (start_point[0] + 1, start_point[1]))
        if field[start_point[0]][start_point[1]] == "\\":
            new_points = get_coords(
                field, "down", (start_point[0] + 1, start_point[1]))
        if field[start_point[0]][start_point[1]] == "/":
            new_points = get_coords(
                field, "up", (start_point[0] - 1, start_point[1]))

    if direction == "left":
        if field[start_point[0]][start_point[1]] in [".", "-"]:
            new_points = get_coords(
                field, "left", (start_point[0], start_point[1] - 1))
        if field[start_point[0]][start_point[1]] == "|":
            new_points = get_coords(
                field, "up", (start_point[0] - 1, start_point[1])) + get_coords(
                field, "down", (start_point[0] + 1, start_point[1]))
        if field[start_point[0]][start_point[1]] == "\\":
            new_points = get_coords(
                field, "up", (start_point[0] - 1, start_point[1]))
        if field[start_point[0]][start_point[1]] == "/":
            new_points = get_coords(
                field, "down", (start_point[0] + 1, start_point[1]))

    if direction == "up":
        if field[start_point[0]][start_point[1]] in [".", "|"]:
            new_points = get_coords(
                field, "up", (start_point[0] - 1, start_point[1]))
        if field[start_point[0]][start_point[1]] == "-":
            new_points = get_coords(
                field, "right", (start_point[0], start_point[1] + 1)) + get_coords(
                field, "left", (start_point[0], start_point[1] - 1))
        if field[start_point[0]][start_point[1]] == "\\":
            new_points = get_coords(
                field, "left", (start_point[0], start_point[1] - 1))
        if field[start_point[0]][start_point[1]] == "/":
            new_points = get_coords(
                field, "right", (start_point[0], start_point[1] + 1))

    if direction == "down":
        if field[start_point[0]][start_point[1]] in [".", "|"]:
            new_points = get_coords(
                field, "down", (start_point[0] + 1, start_point[1]))
        if field[start_point[0]][start_point[1]] == "-":
            new_points = get_coords(
                field, "right", (start_point[0], start_point[1] + 1)) + get_coords(
                field, "left", (start_point[0], start_point[1] - 1))
        if field[start_point[0]][start_point[1]] == "\\":
            new_points = get_coords(
                field, "right", (start_point[0], start_point[1] + 1))
        if field[start_point[0]][start_point[1]] == "/":
            new_points = get_coords(
                field, "left", (start_point[0], start_point[1] - 1))

    result += new_points
    return result


def remove_duplicates(list_of_coords):
    result = []
    for coord in list_of_coords:
        if coord not in result:
            result.append(coord)
    return result


def part2(field):
    global seen
    best = 0
    for i in range(len(field)):
        seen = []
        new = len(remove_duplicates(get_coords(field, "right", (i, 0))))
        if new > best:
            best = new
    for i in range(len(field)):
        seen = []
        new = len(remove_duplicates(get_coords(
            field, "left", (i, len(field[0]) - 1))))
        if new > best:
            best = new
    for i in range(len(field[0])):
        seen = []
        new = len(remove_duplicates(get_coords(field, "down", (0, i))))
        if new > best:
            best = new
    for i in range(len(field[0])):
        seen = []
        new = len(remove_duplicates(get_coords(
            field, "up", (len(field) - 1, i))))
        if new > best:
            best = new
    return best


def part1(field):
    list_of_coords = get_coords(field, "down", (0, 3))

    unique_coords = remove_duplicates(list_of_coords)

    return len(unique_coords)


if __name__ == "__main__":
    with open("day16_input.txt", "r") as f:
        lines = f.readlines()

    field = []
    for line in lines:
        row = []
        for i in range(len(line)-1):
            row.append(line[i])
        field.append(row)

    # solution_part1 = part1(field)
    # print("Solution Part 1: ", solution_part1)

    solution_part2 = part2(field)
    print("Solution Part 2: ", solution_part2)
