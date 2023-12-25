import numpy as np


def calc_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_distances(coords):
    result = []
    for i in range(len(coords)):
        c = coords[i]
        for j in range(i+1, len(coords)):
            result.append(calc_distance(c, coords[j]))
    return result


if __name__ == "__main__":
    with open("day11_input.txt", "r") as f:
        lines = f.readlines()

    a = []
    empyt_rows = []
    for i in range(len(lines)):
        count = 0
        b = []
        for j in range(140):
            b.append(lines[i][j])
            if lines[i][j] == "#":
                count += 1
        a.append(b)
        if count == 0:
            empyt_rows.append(i)

    c = np.array(a)
    d = []
    for line in c.T:
        d.append(list(line))

    e = []
    empty_colums = []
    for i in range(len(d)):
        count = 0
        b = []
        for j in range(len(d[0])):
            b.append(d[i][j])
            if d[i][j] == "#":
                count += 1
        e.append(b)
        if count == 0:
            empty_colums.append(i)

    c = np.array(e)
    d = []
    for line in c.T:
        d.append(list(line))

    print(len(d))
    print(len(d[0]))
    print(empty_colums, empyt_rows)

    coords = []
    for i in range(140):
        for j in range(140):
            if d[i][j] == "#":
                num_rows = 0
                num_cols = 0
                for r in empyt_rows:
                    if i > r:
                        num_rows += 1
                for c in empty_colums:
                    if j > c:
                        num_cols += 1
                x = i + (1000000 - 1) * num_rows
                y = j + (1000000 - 1) * num_cols
                coords.append([x, y])

    distances = get_distances(coords)
    sum = 0
    for d in distances:
        sum += d

    print("Result 1: ", sum)
