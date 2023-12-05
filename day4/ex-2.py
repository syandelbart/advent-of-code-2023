import re


availableCards = {}


def get_card_data(line: str):
    game_data = line[line.find(":") + 2 :]
    [winning_numbers, owned_numbers] = game_data.split(" | ")
    winning_numbers = re.findall(r"\d+", winning_numbers)
    owned_numbers = re.findall(r"\d+", owned_numbers)
    return [winning_numbers, owned_numbers]


def get_total_wins(owned_numbers: list[str], winning_numbers: list[str]):
    won = 0
    points = 1
    for owned_number in owned_numbers:
        if owned_number in winning_numbers:
            points = 1 if won == 0 else points * 2
            won += 1
    return won


with open("./day4/input", "r") as file:
    lines = [line.strip() for line in file]

# Add all cards to availableCards so that we can reuse them
for [index, line] in enumerate(lines):
    [winning_numbers, owned_numbers] = get_card_data(line)
    availableCards[index] = {
        "card_id": index + 1,
        "times_won": get_total_wins(owned_numbers, winning_numbers),
        "amount_received": 1,
    }


for card in availableCards:
    cardData = availableCards[card]

    for x in range(card + 1, card + cardData["times_won"] + 1):
        availableCards[x]["amount_received"] += cardData["amount_received"]

print(
    "Total amount of cards: ",
    sum(map(lambda x: x["amount_received"], availableCards.values())),
)
