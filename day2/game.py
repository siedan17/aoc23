import re

pattern = r'(\d+) (\w+)'

rules = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def valid_game(game: str) -> bool:
    sets = game.split(', ')
    for set in sets:
        match = re.match(pattern, set)
        number = int(match.group(1))
        color = match.group(2)

        if number > rules[color]:
            return False
    return True


def is_valid(line: str) -> int:
    line_split = line.split(': ')
    beginning = line_split[0].split()
    games_string = line_split[1]

    games = games_string.split('; ')  # list of games a string

    for game in games:
        if not valid_game(game):
            return 0

    return int(beginning[1])


if __name__ == "__main__":
    with open("game_input.txt", "r") as f:
        list_of_lines = f.readlines()

    sum = 0
    for line in list_of_lines:
        sum += is_valid(line)

    print("Sum of valid ids: {0:>10d}".format(sum))
