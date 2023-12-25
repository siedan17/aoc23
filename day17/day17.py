
def get_possible_positions(field, current, last_steps):
    return


def get_shortest_path(field):
    result = []
    return result


def part1(field):
    shortest_path = get_shortest_path(field)

    result = 0
    for step in shortest_path:
        result += field[step[0]][step[1]]

    print(len(shortest_path))
    return result


if __name__ == "__main__":
    with open("day17_input.txt", "r") as f:
        lines = f.readlines()

    field = []
    for line in lines:
        row = []
        for i in range(len(line)-1):
            row.append(int(line[i]))
        field.append(row)

    solution_part1 = part1(field)
    print("Solution Part 1: ", solution_part1)

    # solution_part2 = part2(field)
    # print("Solution Part 2: ", solution_part2)
