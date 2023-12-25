

def parse_numbers(lines: [str]) -> tuple[[[int]], [[int]]]:
    winning_numbers = []
    my_numbers = []
    for line in lines:
        w_numbers = line.split(": ")[1].split(" | ")[0].split()
        m_numbers = line.split(": ")[1].split(" | ")[1].split()
        winning_numbers.append([int(number) for number in w_numbers])
        my_numbers.append([int(number) for number in m_numbers])
    return winning_numbers, my_numbers


def calc_num_cards(w_numbers: [[int]], m_numbers: [[int]]) -> int:
    result = 0
    cache = {}
    for i in range(len(w_numbers)):
        counter = 0
        for num in m_numbers[i]:
            if num in w_numbers[i]:
                counter += 1
        cache[i] = [counter, 1]
    for i, value in cache.items():
        result += value[1]
        for j in range(value[0]):
            if i + j + 1 < len(w_numbers):
                cache[i + j + 1][1] += value[1]

    return result


if __name__ == "__main__":
    with open("scratchcards_input.txt", "r") as f:
        list_of_lines = f.readlines()

    winning_numbers, my_numbers = parse_numbers(list_of_lines)
    assert len(winning_numbers) == len(my_numbers)

    total_cards = calc_num_cards(winning_numbers, my_numbers)
    print("Result is: ", total_cards)
