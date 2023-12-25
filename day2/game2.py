import re

pattern = r'(\d+) (\w+)'


def minimum_set(games: [str]) -> dict:
    result = {"red": 1, "blue": 1, "green": 1}
    for game in games:
        sets = game.split(', ')
        for set in sets:
            match = re.match(pattern, set)
            number = int(match.group(1))
            color = match.group(2)

            if number > result[color]:
                result[color] = number

    return result


def power_of(line: str) -> int:
    line_split = line.split(': ')
    games_string = line_split[1]

    games = games_string.split('; ')  # list of games a string
    min_set = minimum_set(games)

    return min_set['red'] * min_set['blue'] * min_set['green']


if __name__ == "__main__":
    with open("game_input.txt", "r") as f:
        list_of_lines = f.readlines()

    sum = 0
    for line in list_of_lines:
        sum += power_of(line)

    print(f"Sum of powers: {sum:>8d}")
