import re


data_mappings = {}

with open("./day5/input", "r") as file:
    lines = [line.strip() for line in file]

seeds_list = lines[0][lines[0].find(":") + 2 :].split(" ")

current_map = ""
for line in lines[1:]:
    if line == "":
        continue
    parts = re.findall(r"\w+", line)
    if re.match(r"[a-z]+", parts[0]):
        current_map = parts[0] + "-" + parts[2]
        data_mappings[current_map] = []

    else:
        parts = [int(x) for x in parts]

        data_mappings[current_map].append(
            {"destination": parts[0], "source": parts[1], "range": parts[2]}
        )


procedure = [
    "seed",
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
]

seed_locations = {}
for seed in seeds_list:
    seed_locations[seed] = {"seed": int(seed)}
    for x in range(0, len(procedure) - 1):
        map_key = procedure[x] + "-" + procedure[x + 1]
        current_value = seed_locations[seed][procedure[x]]
        seed_locations[seed][procedure[x + 1]] = current_value
        for mapping in data_mappings[map_key]:
            if (
                mapping["source"]
                <= current_value
                < mapping["source"] + mapping["range"]
            ):
                seed_locations[seed][procedure[x + 1]] = (
                    mapping["destination"] + current_value - mapping["source"]
                )
                break

print("Lowest location:", min(map(lambda x: x["location"], seed_locations.values())))
