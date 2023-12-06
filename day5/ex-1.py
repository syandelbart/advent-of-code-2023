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
    print(parts)
    if re.match(r"[a-z]+", parts[0]):
        current_map = parts[0] + "-" + parts[2]
        data_mappings[current_map] = {}
    else:
        parts = [int(x) for x in parts]

        for [index, x] in enumerate(range(parts[1], parts[1] + parts[2])):
            data_mappings[current_map][str(x)] = str(parts[0] + index)


# for key in data_mappings:
#     print(key)
#     for x in sorted(data_mappings[key], key=lambda x: data_mappings[key][x]):
#         print(x, data_mappings[key][x])


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
    seed_locations[seed] = {"seed": seed}
    for x in range(0, len(procedure) - 1):
        map_key = procedure[x] + "-" + procedure[x + 1]

        if seed_locations[seed][procedure[x]] not in data_mappings[map_key]:
            current_value = seed_locations[seed][procedure[x]]
        else:
            current_value = data_mappings[map_key][seed_locations[seed][procedure[x]]]

        seed_locations[seed][procedure[x + 1]] = current_value

print("Lowest location:", min(map(lambda x: x["location"], seed_locations.values())))
