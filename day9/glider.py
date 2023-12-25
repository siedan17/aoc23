

def all_zeros(a: [int]) -> bool:
    for i in a:
        if i != 0:
            return False
    return True


def get_diff(hist: [int]) -> [int]:
    result = []
    for i in range(len(hist) - 1):
        result.append(hist[i + 1] - hist[i])
    return result


def get_next(hist: [int]) -> int:
    if all_zeros(hist):
        return 0

    if len(hist) == 1:
        return hist[-1]

    return hist[-1] + get_next(get_diff(hist))


def get_prev(hist: [int]) -> int:
    if all_zeros(hist):
        return 0

    if len(hist) == 1:
        return hist[0]

    return hist[0] - get_prev(get_diff(hist))


if __name__ == "__main__":
    with open("glider_input.txt", "r") as f:
        lines = f.readlines()
        histories = [[int(a) for a in line.split()] for line in lines]

        sum_next = 0
        for history in histories:
            sum_next += get_next(history)
        print("Result Part 1: ", sum_next)

        sum_prev = 0
        for history in histories:
            sum_prev += get_prev(history)
        print("Result Part 2: ", sum_prev)
