
def get_seed(loc: int) -> int:
    hum = get_prev(loc, humidity_location)
    temp = get_prev(hum, temperature_humidity)
    light = get_prev(temp, light_temperature)
    water = get_prev(light, water_light)
    fert = get_prev(water, fertilizer_water)
    soil = get_prev(fert, soil_fertilizer)
    seed = get_prev(soil, seed_soil)
    return seed


def check_seed(seed, seeds):
    for i in range(len(seeds)):
        if i % 2 != 0:
            continue
        if seeds[i] <= seed < seeds[i] + seeds[i+1]:
            return True
    return False


def get_prev(next, intervals):
    for interval in intervals:
        prev = next - (interval[0] - interval[1])
        if interval[1] <= prev < interval[1] + interval[2]:
            return prev
    return next


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

    location = 30_000_000  # from solution.
    seed = get_seed(location)
    while not check_seed(seed, seeds):
        location += 1
        seed = get_seed(location)

    print("loc: ", location)
    # 5 minute solution.
