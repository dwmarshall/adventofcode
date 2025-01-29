import sys


class BingoCard:
    def __init__(self, card: list[list[int]]):
        assert len(card) == 5
        assert all(len(row) == 5 for row in card)
        self.vectors = [set(row) for row in card] + [set(col) for col in zip(*card)]
        self.numbers = {num for row in card for num in row}

    def call_number(self, n: int) -> None:
        for v in self.vectors:
            v.discard(n)
        self.numbers.discard(n)

    def bingo(self) -> bool:
        return any(len(v) == 0 for v in self.vectors)

    def remaining_sum(self) -> int:
        return sum(self.numbers)


def read_input(filename: str) -> tuple[list[int], list[BingoCard]]:
    with open(sys.argv[1], "r") as file:
        called_numbers = map(int, file.readline().strip().split(","))
        cards = []
        while file.readline():  # discard an empty line
            card = [list(map(int, file.readline().split())) for _ in range(5)]
            cards.append(BingoCard(card))
    return called_numbers, cards


def part1(filename: str) -> None:
    called_numbers, cards = read_input(filename)
    for n in called_numbers:
        for c in cards:
            c.call_number(n)
        if winners := [c for c in cards if c.bingo()]:
            print(f"Part 1: The product is {n * winners[0].remaining_sum()}")
            return


def part2(filename: str) -> None:
    called_numbers, cards = read_input(filename)
    for n in called_numbers:
        for c in cards:
            c.call_number(n)
        bingos = [c for c in cards if c.bingo()]
        if len(cards) == 1 and len(bingos) == 1:
            print(f"Part 2: The product is {n * cards[0].remaining_sum()}")
            return
        else:
            cards = [c for c in cards if not c.bingo()]


if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])
