import copy
import time

def get_ranges(brick):
    return [min(brick[0][0], brick[1][0]), max(brick[0][0], brick[1][0])], [min(brick[0][1], brick[1][1]), max(brick[0][1], brick[1][1])], [min(brick[0][2], brick[1][2]), max(brick[0][2], brick[1][2])]

def overlap(range1, range2):
    if range1[0] > range2[1] or range1[1] < range2[0]:
        return False
    return True

def get_beneath_map(map):
    result = {}
    for key, brick in map.items():
        x_range, y_range, z_range = get_ranges(brick)
        beneath_list = []
        for trial_brick in map.values():
            if trial_brick != brick:
                x_range_trial, y_range_trial, z_range_trial = get_ranges(trial_brick)
                if (overlap(x_range, x_range_trial) and overlap(y_range, y_range_trial)) and z_range_trial[1] <= z_range[0]:
                    beneath_list.append(trial_brick)
        result[key] = beneath_list
    return result

def get_z_position(map, brick):
    x_range, y_range, z_range = get_ranges(brick)
    max_z_value = 0
    for trial_brick in map.values():
        x_range_trial, y_range_trial, z_range_trial = get_ranges(trial_brick)
        if (overlap(x_range, x_range_trial) and overlap(y_range, y_range_trial)) and z_range_trial[1] <= z_range[0]:
            if z_range_trial[1] > max_z_value:
                max_z_value = z_range_trial[1]
    return [max_z_value + 1, max_z_value + 1 + z_range[1] - z_range[0]]

def shift_down(map):
    copy_map = copy.deepcopy(map)
    new_map = {}
    while len(list(copy_map.keys())) > 0:
        beneath_map = get_beneath_map(copy_map)
        for k, v in beneath_map.items():
            if len(v) == 0:
                z_position = get_z_position(new_map, copy_map[k])
                new_map[k] = copy.deepcopy(copy_map)[k]
                new_map[k][0][2] = z_position[0]
                new_map[k][1][2] = z_position[1]
                copy_map.pop(k)
    return new_map

def get_direct_beneath_map(map):
    copy_map = copy.deepcopy(map)
    result = {}
    for key, brick in copy_map.items():
        x_range, y_range, z_range = get_ranges(brick)
        beneath_list = []
        for k, trial_brick in copy_map.items():
            if trial_brick != brick:
                x_range_trial, y_range_trial, z_range_trial = get_ranges(trial_brick)
                if (overlap(x_range, x_range_trial) and overlap(y_range, y_range_trial)) and z_range_trial[1] + 1 == z_range[0]:
                    beneath_list.append(k)
        result[key] = beneath_list
    return result

def get_direct_over_map(map):
    result = {}
    for key, brick in map.items():
        x_range, y_range, z_range = get_ranges(brick)
        beneath_list = []
        for k, trial_brick in map.items():
            if trial_brick != brick:
                x_range_trial, y_range_trial, z_range_trial = get_ranges(trial_brick)
                if (overlap(x_range, x_range_trial) and overlap(y_range, y_range_trial)) and z_range_trial[0] - 1 == z_range[1]:
                    beneath_list.append(k)
        result[key] = beneath_list
    return result

def part1(map, under, over):
    list_of_disintegrate = []
    for k in map.keys():
        if len(over[k]) == 0:
            list_of_disintegrate.append(k)
            continue
        can_disintegrate = True
        for o in over[k]:
            if len(under[o]) < 2:
                can_disintegrate = False
        if can_disintegrate:
            list_of_disintegrate.append(k)
    return list_of_disintegrate

def part2(map, under, over):
    counter = 0
    for key in map.keys():
        curr_sum = []
        curr_breaking_bricks = [key]
        while len(curr_breaking_bricks) > 0:
            new_breaking_bricks = []
            for brick in curr_breaking_bricks:
                for trial_brick_key in over[brick]:
                    is_breaking = True
                    for below_brick in under[trial_brick_key]:
                        if below_brick not in curr_sum and below_brick != key:
                            is_breaking = False
                    if is_breaking:
                        new_breaking_bricks.append(trial_brick_key)

            for brick in new_breaking_bricks:
                if brick not in curr_sum:
                    curr_sum.append(brick)

            curr_breaking_bricks = new_breaking_bricks
        
        counter += len(curr_sum)
    return counter

if __name__ == "__main__":
    with open("day22_input.txt", "r") as f:
        lines = f.readlines()
    
    map = {}
    for i in range(len(lines)):
        line = lines[i].strip().split("~")
        first = [int(j) for j in line[0].split(",")]
        second = [int(j) for j in line[1].split(",")]
        map[i] = [first, second]
    
    start = time.time()
    shifted = shift_down(map)
    print("after shifted: ", time.time() - start)
    under = get_direct_beneath_map(shifted)
    over = get_direct_over_map(shifted)
    print("time after over, under: ", time.time() - start)

    sol = part1(shifted, under, over)
    print("Solution Part 1: ", len(sol))
    print("after all: ", time.time() - start)

    print("Solution Part 2: ", part2(shifted, under, over))

    
