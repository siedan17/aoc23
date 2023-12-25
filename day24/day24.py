def find_intersection(l1, l2):
    x1, y1, dx1, dy1 = l1
    x2, y2, dx2, dy2 = l2

    # Calculate the determinant
    det = dx1 * dy2 - dx2 * dy1

    if det == 0:
        return (0, 0)  # Lines are parallel, no intersection

    t = ((x2 - x1) * dy2 - (y2 - y1) * dx2) / det
    s = ((x2 - x1) * dy1 - (y2 - y1) * dx1) / det

    if t >= 0 and s >= 0:
        intersection_x = x1 + t * dx1
        intersection_y = y1 + t * dy1
        return intersection_x, intersection_y
    else:
        return (0, 0)  # Lines meet in past


def is_intersecting(l1, l2):
    point = find_intersection(l1, l2)
    for p in point:
        if not (200_000_000_000_000 <= p <= 400_000_000_000_000):
            return False
    return True


def part1(lines):
    result = 0
    for i in range(len(lines) - 1):
        l1 = lines[i]
        for l2 in lines[i + 1:]:
            if is_intersecting(l1, l2):
                result += 1
    return result


if __name__ == "__main__":
    with open("day24_input.txt", "r") as f:
        lines = f.readlines()

    input_lines = []
    for line in lines:
        line = line.strip()
        a = line.split(" @ ")
        b = [int(x) for x in a[0].split(", ")]
        c = [int(x) for x in a[1].split(", ")]
        new_line = [b[0], b[1], c[0], c[1]]
        input_lines.append(new_line)

    solution_part1 = part1(input_lines)
    print("Solution Part 1: ", solution_part1)
