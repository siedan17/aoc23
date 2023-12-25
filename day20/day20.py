
import math

def part1(lines):
    mappings = dict((a, b) for (a, b) in lines)

    # For any conjunction modules we must initialize inputs
    for k, v in mappings.items():
        if v[2]:
            for a, b in mappings.items():
                if k in b[0]:
                    v[3][a] = False # default state (down == False)

    global_low = 0
    global_high = 0
    for _ in range(1000):
        low = 0
        high = 0
        queue = [("broadcaster", 0, None)] # 0 == low; 1 == high
        while queue:
            (curr, signal, input) = queue.pop(0)

            if signal:
                high += 1
            else:
                low += 1

            if curr not in mappings:
                continue

            [targets, is_ff, is_con, state] = mappings[curr]

            if is_ff:
                if not signal:
                    if state:
                        mappings[curr][3] = False
                        new_signal = 0
                    else:
                        mappings[curr][3] = True
                        new_signal = 1

                    for target in targets:
                        queue.append((target, new_signal, curr))
            elif is_con:
                state[input] = bool(signal)
                if all(state.values()):
                    new_signal = 0
                else:
                    new_signal = 1
                for target in targets:
                    queue.append((target, new_signal, curr))
            else: # just for broadcaster
                for target in targets:
                    queue.append((target, signal, curr))
        # print(high, low) # for cycle detection
        global_low += low
        global_high += high

    print(global_high, global_low)
    return global_high * global_low

def part2(lines):
    mappings = dict((a, b) for (a, b) in lines)
    for k, v in mappings.items():
        if v[2]:
            for a, b in mappings.items():
                if k in b[0]:
                    v[3][a] = False

    lowest_parents = {
        "kd": None,
        "zf": None,
        "vg": None,
        "gs": None,
    }

    curr_cycle = 0
    answer = 0
    while True:
        if all(val is not None for val in lowest_parents.values()):
            answer = math.lcm(*list(lowest_parents.values()))
            break

        curr_cycle += 1
        queue = [("broadcaster", 0, None)]
        while queue:
            (curr, signal, input) = queue.pop(0) # wohin, was, von wo.

            if curr in lowest_parents and not signal:
                    print(curr, signal, input, curr_cycle)
                    lowest_parents[curr] = curr_cycle

            if curr not in mappings:
                continue

            [targets, is_ff, is_con, state] = mappings[curr]

            if is_ff:
                if not signal:
                    if state:
                        mappings[curr][3] = False
                        new_signal = 0
                    else:
                        mappings[curr][3] = True
                        new_signal = 1

                    for target in targets:
                        queue.append((target, new_signal, curr))
            elif is_con:
                state[input] = bool(signal)
                if all(state.values()):
                    new_signal = 0
                else:
                    new_signal = 1
                for target in targets:
                    queue.append((target, new_signal, curr))
            else:
                for target in targets:
                    queue.append((target, signal, curr))

    return answer

if __name__ == "__main__":
    with open("day20_input.txt", "r") as f:
        input_lines = f.readlines()
    lines = []
    for line in input_lines:
        line = line.strip()
        split = line.split(" -> ")

        name = split[0]
        flip_flop = name.startswith("%")
        conjunction = name.startswith("&")
        target = split[1].split(", ")

        if flip_flop:
            state = False
            name = split[0][1:]
        elif conjunction:
            state = {}
            name = split[0][1:]
        else:
            state = None
        
        val = (name, [target, flip_flop, conjunction, state])
        lines.append(val)
    
    # solution1 = part1(lines)
    # print("Solution Part 1: ", solution1)

    solution2 = part2(lines)
    print("Solution Part 2: ", solution2)

