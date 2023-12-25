
COLUMNS = 140  # looked up from input
ROWS = 140  # looked up from input


def parse_numbers(lines: [str]) -> [[int]]:
    result = []
    for i in range(ROWS):
        idx = 0
        while idx < COLUMNS:
            if not lines[i][idx] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                idx += 1
                continue
            number = [i, idx]
            counter = 1
            while lines[i][idx + counter] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                counter += 1
            number.append(idx + counter)  # from to in python indexing
            result.append(number)
            idx += counter
    print(len(result))
    return result


def parse_stars(lines: [str]) -> [[int]]:
    result = []
    for i in range(ROWS):
        for j in range(COLUMNS):
            if lines[i][j] == "*":
                result.append([i, j])
    print(len(result))
    return result


def find_gears(numbers: [[int]], stars: [[int]]) -> [[int]]:
    result = []
    for star in stars:
        adjacent_nums = []
        for number in numbers:
            if star[0] - 1 <= number[0] <= star[0] + 1:
                if number[1] - 1 <= star[1] <= number[2]:
                    adjacent_nums.append(number)

        if len(adjacent_nums) == 2:
            result.append(adjacent_nums)
    print(len(result))
    return result


def multiply_sum_gears(gears: [[[int, int]]], lines: [str]) -> int:
    sum = 0
    for gear in gears:
        gear1 = int(lines[gear[0][0]][gear[0][1]:gear[0][2]])
        gear2 = int(lines[gear[1][0]][gear[1][1]:gear[1][2]])
        sum += gear1 * gear2
    return sum


if __name__ == "__main__":
    with open("gear_input.txt", "r") as f:
        list_of_lines = f.readlines()

        parsed_numbers = parse_numbers(list_of_lines)

        parsed_stars = parse_stars(list_of_lines)

        gears = find_gears(parsed_numbers, parsed_stars)

        sum_of_products = multiply_sum_gears(gears, list_of_lines)

        print("Result is: ", sum_of_products)
