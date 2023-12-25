import math


def get_steps(map, instructions, start):
    key = start
    counter = 0
    z_counter = 0
    while key[-1] != "Z" or z_counter < 3:
        key = map[key][instructions[counter % len(instructions)]]
        if key[-1] == "Z":
            z_counter += 1
        counter += 1
    return counter


if __name__ == "__main__":
    map_dict = {}
    instruction_string = ""
    instructions = []
    start_positions = []
    end_positions = []

    with open("map_input.txt", "r") as f:
        lines = f.readlines()
        instruction_string = lines[0]
        for l in instruction_string:
            if l == "R":
                instructions.append(1)
            elif l == "L":
                instructions.append(0)
        for line in lines[1:]:
            a = line.split(" = ")
            c = a[1][1:-2].split(", ")
            map_dict[a[0]] = [c[0], c[1]]

        for key in map_dict.keys():
            if key[-1] == "A":
                start_positions.append(key)

        steps = []
        for start in start_positions:
            steps.append(get_steps(map_dict, instructions, start))
        result = math.lcm(*steps)
        print("result: ", result)
