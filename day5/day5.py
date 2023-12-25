
def get_loc(seed: int) -> int:
    soil = get_next(seed, seed_soil)
    fertilizer = get_next(soil, soil_fertilizer)
    water = get_next(fertilizer, fertilizer_water)
    light = get_next(water, water_light)
    temp = get_next(light, light_temperature)
    hum = get_next(temp, temperature_humidity)
    loc = get_next(hum, humidity_location)
    return loc


def get_next(prev, intervals):
    for interval in intervals:
        if interval[1] <= prev < interval[1] + interval[2]:
            return prev + (interval[0] - interval[1])
    return prev


if __name__ == "__main__":
    seeds = []
    seed_soil = []
    soil_fertilizer = []
    fertilizer_water = []
    water_light = []
    light_temperature = []
    temperature_humidity = []
    humidity_location = []
    with open("day5_input.txt", "r") as f:
        lines = f.readlines()
    counter = 0
    while counter < len(lines):
        if "seeds" in lines[counter]:
            a = lines[counter].split(": ")
            b = a[1].split()
            for i in b:
                seeds.append(int(i))
            counter += 1
            continue
        if "seed-to-soil" in lines[counter]:
            counter += 1
            while ":" not in lines[counter]:
                a = lines[counter].split()
                if len(a) > 0:
                    seed_soil.append([int(i) for i in a])
                counter += 1
            continue
        if "soil-to-fertilizer" in lines[counter]:
            counter += 1
            while ":" not in lines[counter]:
                a = lines[counter].split()
                if len(a) > 0:
                    soil_fertilizer.append([int(i) for i in a])
                counter += 1
            continue
        if "fertilizer-to-water" in lines[counter]:
            counter += 1
            while ":" not in lines[counter]:
                a = lines[counter].split()
                if len(a) > 0:
                    fertilizer_water.append([int(i) for i in a])
                counter += 1
            continue
        if "water-to-light" in lines[counter]:
            counter += 1
            while ":" not in lines[counter]:
                a = lines[counter].split()
                if len(a) > 0:
                    water_light.append([int(i) for i in a])
                counter += 1
            continue

        if "light-to-temperature" in lines[counter]:
            counter += 1
            while ":" not in lines[counter]:
                a = lines[counter].split()
                if len(a) > 0:
                    light_temperature.append([int(i) for i in a])
                counter += 1
            continue

        if "temperature-to-humidity" in lines[counter]:
            counter += 1
            while ":" not in lines[counter]:
                a = lines[counter].split()
                if len(a) > 0:
                    temperature_humidity.append([int(i) for i in a])
                counter += 1
            continue

        if "humidity-to-location" in lines[counter]:
            counter += 1
            while counter < len(lines):
                a = lines[counter].split()
                if len(a) > 0:
                    humidity_location.append([int(i) for i in a])
                counter += 1
            continue
        counter += 1

    locs = []
    for seed in seeds:
        locs.append(get_loc(seed))

    min = locs[0]
    for loc in locs:
        if loc < min:
            min = loc

    print(len(locs) == len(seeds))
    print("solution is: ", min)
