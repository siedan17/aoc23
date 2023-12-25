
COLUMNS = 140  # looked up from input
ROWS = 140  # looked up from input


def parse_numbers(lines: [str]) -> [[int]]:
    result = []
    for i in range(len(lines)):
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


def check_numbers(parsed: [[int]], lines: [str]) -> [[int]]:
    result = []
    for number in parsed:
        row_idx = number[0]
        left_idx = number[1]
        right_idx = number[2]
        if left_idx > 0:
            left_idx = number[1] - 1
        if right_idx < COLUMNS:
            right_idx = number[2] + 1
        # check in same line:
        if number[1] != left_idx:
            if lines[row_idx][left_idx] != '.':
                result.append(number)
                continue
        if number[2] != right_idx:
            # indexing in python! therefore -1.
            if lines[row_idx][right_idx - 1] != '.':
                result.append(number)
                continue
        # check above:
        appended = False
        if row_idx > 0:
            for character in lines[row_idx - 1][left_idx:right_idx]:
                if character != '.':
                    result.append(number)
                    appended = True
                    break

        if appended:
            continue
        # check below:
        if row_idx < ROWS - 1:
            for character in lines[row_idx + 1][left_idx:right_idx]:
                if character != '.':
                    result.append(number)
                    break
    print(len(result))
    return result


def sum_numbers(valid_numbers: [[int]], lines: [str]) -> int:
    sum = 0
    for number in valid_numbers:
        sum += int(lines[number[0]][number[1]:number[2]])
    return sum


if __name__ == "__main__":
    with open("gear_input.txt", "r") as f:
        list_of_lines = f.readlines()

        parsed_numbers = parse_numbers(list_of_lines)

        valid_numbers = check_numbers(parsed_numbers, list_of_lines)

        sum_of_valid_numbers = sum_numbers(valid_numbers, list_of_lines)

        print("Result is: ", sum_of_valid_numbers)
