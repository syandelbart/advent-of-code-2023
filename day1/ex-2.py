import regex as re

numbersAsSpeech = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

searchPattern = "|".join(numbersAsSpeech.keys()) + r"|\d"
print(searchPattern)

sum = 0
for line in open("./day1/input", "r"):
    matches: list[str] = re.findall(searchPattern, line, overlapped=True)
    valueFromDictFirst = numbersAsSpeech.get(matches[0])
    valueFromDictLast = numbersAsSpeech.get(matches[-1])
    value = (valueFromDictFirst if valueFromDictFirst is not None else matches[0]) + (
        valueFromDictLast if valueFromDictLast is not None else matches[-1]
    )

    print(matches, matches[0], matches[-1], value)

    sum += int(value)
print("Total sum:", sum)
