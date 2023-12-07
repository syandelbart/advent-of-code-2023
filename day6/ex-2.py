with open("./day6/input", "r") as file:
    lines = [line.strip() for line in file]


def get_race_wins_time_to_hold(time: int, record: int):
    wins = []
    for hold_time in range(0, time):
        if (time - hold_time) * hold_time > record:
            wins.append(hold_time)
    return wins


# We combine the string values of all the numbers together and make a list of this singular large number
times = [int(lines[0][lines[0].find(":") + 1 :].replace(" ", ""))]
distances = [int(lines[1][lines[1].find(":") + 1 :].replace(" ", ""))]

value = 1
for race_num in range(0, len(times)):
    time = times[race_num]
    distance = distances[race_num]

    wins = get_race_wins_time_to_hold(time, distance)
    value *= len(wins)
print("Total multiplied: ", value)
