
DIGIT_DICT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
}


def parse_line(line: str) -> [int]:
    numbers = []
    idx = 0
    while idx < len(line):
        try:
            numbers.append(int(line[idx]))
            idx += 1
            continue
        except ValueError:
            pass

        appended = False
        for key in DIGIT_DICT.keys():
            if idx + len(key) > len(line):
                continue
            if key == line[idx:idx+len(key)]:
                numbers.append(DIGIT_DICT[key])
                idx += 1
                appended = True
                break

        if appended:
            continue
        idx += 1
    return numbers


def get_list_of_numbers(lines: [str]) -> [int]:
    result = []
    for line in lines:
        numbers = parse_line(line)

        if len(numbers) > 1:
            result.append(10 * numbers[0] + numbers[-1])
        elif len(numbers) == 1:
            result.append(10 * numbers[0] + numbers[0])
        else:
            print("no numbers!")
    return result


def get_sum(numbers: [int]) -> int:
    sum = 0
    for num in numbers:
        sum += num
    return sum


if __name__ == "__main__":
    with open("cal_input.txt", "r") as f:
        list_of_lines = f.readlines()

    numbers = get_list_of_numbers(list_of_lines)
    print(len(numbers))

    print("Result is: ", get_sum(numbers))
