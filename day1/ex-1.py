import re

sum = 0
for line in open("./day1/input", "r"):
    matches: list[str] = re.findall(r"\d", line)
    value = matches[0] + matches[-1]
    sum += int(value)
print("Total sum:", sum)
