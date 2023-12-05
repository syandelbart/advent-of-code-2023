import re

AMOUNT_ALLOWED = {"red": 12, "green": 13, "blue": 14}


def game_is_possible(line: str):
    print(line)
    game_data = line[line.find(":") + 2 :]
    game_sets = game_data.split("; ")
    # We will keep the highest amount of cubes here
    most_cubes_needed = {}
    for game_set in game_sets:
        entries: list[str] = re.findall(r"\d+ (?:blue|green|red)", game_set)
        for entry in entries:
            [number, color] = entry.split(" ")
            if most_cubes_needed.get(color) is None or most_cubes_needed.get(
                color
            ) < int(number):
                most_cubes_needed[color] = int(number)
    return (
        (most_cubes_needed["red"] if most_cubes_needed["red"] is not None else 1)
        * (most_cubes_needed["blue"] if most_cubes_needed["blue"] is not None else 1)
        * (most_cubes_needed["green"] if most_cubes_needed["green"] is not None else 1)
    )


with open("./day2/input", "r") as file:
    lines = [line.strip() for line in file]

gameList = map(game_is_possible, lines)

sum = sum(gameList)
print("Total sum:", sum)
