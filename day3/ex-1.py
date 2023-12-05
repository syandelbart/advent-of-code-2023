import re


def number_adjecent_to_symbol(
    number_start_x, number_start_y, number_end_x, number_end_y, m
):
    word_x_start = max(number_start_x - 1, 0)
    word_x_end = min(number_end_x + 1, line_length)
    word_y_start = max(number_start_y - 1, 0)
    word_y_end = min(number_end_y + 2, len(lines))

    # print(word_x_start, word_x_end, word_y_start, word_y_end)

    for y in range(word_y_start, word_y_end):
        for x in range(word_x_start, word_x_end):
            if y == number_start_y and x >= number_start_x and x < number_end_x:
                continue
            # print(lines[y][x], end="")
            if re.search(symbol_regex, lines[y][x]) is not None:
                # print(" FOUNDSYMBOL ")
                return True
        # print()

    print(m.group(0), m.start(0), m.end(0))
    for y in range(word_y_start, word_y_end):
        for x in range(word_x_start, word_x_end):
            print(lines[y][x], end="")

            if re.search(symbol_regex, lines[y][x]) is not None:
                print(" FOUNDSYMBOL ")
        print()
    print("---------")
    return False


with open("./day3/input", "r") as file:
    lines = [line.strip() for line in file]

line_length = len(lines[0])
symbol_regex = r"[%$*#+&@=\/\-]"
sum = 0
for [index, line] in enumerate(lines):
    numbers = re.finditer(r"\d+", line)
    for number in numbers:
        number_start_x = number.start(0)
        number_end_x = number.end(0)
        number_start_y = index
        number_end_y = index

        if number_adjecent_to_symbol(
            number_start_x, number_start_y, number_end_x, number_end_y, number
        ):
            sum += int(number.group(0))
print(sum)
