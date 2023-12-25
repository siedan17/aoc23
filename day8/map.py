
def get_steps(map, instructions):
    key = "AAA"
    counter = 0
    list_of_keys = []
    while key != "ZZZ":
        list_of_keys.append(key)
        key = map[key][instructions[counter % len(instructions)]]
        counter += 1
    return counter


if __name__ == "__main__":
    map_dict = {}
    instruction_string = ""
    instructions = []

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

        num_steps = get_steps(map_dict, instructions)
        print("result: ", num_steps)
