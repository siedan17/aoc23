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
    for line in lines:
        count = 0
        b = []
        for i in range(140):
            b.append(line[i])
            if line[i] == "#":
                count += 1
        a.append(b)
        if count == 0:
            a.append(["." for j in range(140)])

    c = np.array(a)
    d = []
    for line in c.T:
        d.append(list(line))

    e = []
    counts = []
    for line in d:
        count = 0
        b = []
        for i in range(149):
            b.append(line[i])
            if line[i] == "#":
                count += 1
        e.append(b)
        counts.append(count)
        if count == 0:
            e.append(["." for j in range(149)])

    c = np.array(e)
    d = []
    for line in c.T:
        d.append(list(line))

    coords = []
    for i in range(149):
        for j in range(148):
            if d[i][j] == "#":
                coords.append([i, j])

    distances = get_distances(coords)

    sum = 0
    for d in distances:
        sum += d

    print("Result 1: ", sum)
