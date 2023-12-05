import re

AMOUNT_ALLOWED = {"red": 12, "green": 13, "blue": 14}


def game_is_possible(line: str):
    print(line)
    game_data = line[line.find(":") + 2 :]
    game_sets = game_data.split("; ")
    for game_set in game_sets:
        entries: list[str] = re.findall(r"\d+ (?:blue|green|red)", game_set)
        for entry in entries:
            [number, color] = entry.split(" ")
            if AMOUNT_ALLOWED[color] < int(number):
                return False
    return True


with open("./day2/input", "r") as file:
    lines = [line.strip() for line in file]

gameList = map(game_is_possible, lines)

sum = 0
for [index, entry] in enumerate(gameList):
    if entry:
        sum += index + 1
print("Total sum:", sum)
