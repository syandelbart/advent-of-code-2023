import re


def get_total_points(line: str):
    game_data = line[line.find(":") + 2 :]
    [winning_numbers, owned_numbers] = game_data.split(" | ")
    winning_numbers = re.findall(r"\d+", winning_numbers)
    owned_numbers = re.findall(r"\d+", owned_numbers)

    won = 0
    points = 1
    for owned_number in owned_numbers:
        if owned_number in winning_numbers:
            points = 1 if won == 0 else points * 2
            won += 1
    return points if won > 0 else 0


with open("./day4/input", "r") as file:
    lines = [line.strip() for line in file]

cardList = map(get_total_points, lines)

sum = 0
for entry in cardList:
    sum += entry
print("Total sum:", sum)
