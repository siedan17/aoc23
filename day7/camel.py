import numpy as np


def get_type(hand: str) -> int:
    h_dict = {}
    j_num = 0
    for h in hand:
        if h == "J":
            j_num += 1
        try:
            h_dict[h] += 1
        except KeyError:
            h_dict[h] = 1
    arr = np.array(list(h_dict.values()))

    if j_num == 5:
        return 7
    if max(arr) == j_num:
        maximum = np.sort(arr)[len(h_dict.keys())-2]
    else:
        maximum = max(arr)

    if min(arr) == j_num:
        minimum = np.sort(arr)[1]
    else:
        minimum = min(arr)

    if maximum + j_num == 5:
        return 7
    if maximum + j_num == 4:
        return 6
    if maximum + j_num == 3 and minimum == 2:
        return 5
    if maximum + j_num == 3 and minimum == 1:
        return 4
    if maximum + j_num == 2 and len(arr) == 3:
        return 3
    if maximum + j_num == 2 and len(arr) - j_num == 4:
        return 2
    if maximum == 1 and j_num == 0:
        return 1
    print(arr, h_dict)
    return 0


def get_higher(hand1: str, hand2: str) -> bool:
    letters = {
        "A": 15,
        "K": 14,
        "Q": 13,
        "J": 0,
        "T": 11,
    }
    numbers1 = []
    numbers2 = []
    for i in range(len(hand1)):
        try:
            numbers1.append(int(hand1[i]))
        except ValueError:
            numbers1.append(letters[hand1[i]])
        try:
            numbers2.append(int(hand2[i]))
        except ValueError:
            numbers2.append(letters[hand2[i]])

    for j in range(len(numbers1)):
        if numbers1[j] > numbers2[j]:
            return True
        if numbers2[j] > numbers1[j]:
            return False
    return True


def compare(hand1: str, hand2: str) -> bool:  # true if first is stronger! false otherwise
    type1 = get_type(hand1)
    type2 = get_type(hand2)
    # print("types: ", type1, type2)

    if type1 == type2:
        return get_higher(hand1, hand2)
    return type1 > type2


def sort_hands(hands: [str]) -> [str]:
    if len(hands) == 1:
        return hands
    if len(hands) == 2:
        if compare(hands[0], hands[1]):
            return [hands[1], hands[0]]
        return hands

    left = hands[:int(len(hands)/2)]
    right = hands[int(len(hands)/2):]

    sorted_left = sort_hands(left)
    sorted_right = sort_hands(right)
    # print(sorted_left, sorted_right)
    # print('____')

    left_idx = 0
    right_idx = 0
    sorted_list = []
    while left_idx < len(sorted_left) and right_idx < len(sorted_right):
        if compare(sorted_left[left_idx], sorted_right[right_idx]):
            sorted_list.append(sorted_right[right_idx])
            right_idx += 1
        else:
            sorted_list.append(sorted_left[left_idx])
            left_idx += 1
    if left_idx < len(sorted_left):
        for i in sorted_left[left_idx:]:
            sorted_list.append(i)
    else:
        for i in sorted_right[right_idx:]:
            sorted_list.append(i)
    return sorted_list


if __name__ == "__main__":
    with open("camel_input.txt", "r") as f:
        lines = f.readlines()
        lines_dict = {}
        for line in lines:
            s = line.split()
            lines_dict[s[0]] = int(s[1])

        # print(lines_dict)

        key_list = list(lines_dict.keys())

        sorted_keys = sort_hands(key_list)

        # print(sorted_keys)

        result = 0

        for i in range(len(sorted_keys)):
            result += (i+1) * lines_dict[sorted_keys[i]]

        print("result: ", result)
