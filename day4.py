import re


def part1(_input_):
    cards = _input_.splitlines()

    result = 0

    for line in cards:
        groups = re.search(r"Card\s+\d+: ([\d\s]+)\| ([\d\s]+)", line)
        winners = list(map(int, groups.group(1).split()))
        numbers = list(map(int, groups.group(2).split()))

        matches = 0
        for winner in winners:
            if winner in numbers:
                matches += 1

        score = 0 if matches == 0 else 1
        for i in range(matches - 1):
            score *= 2

        result += score

    return result


def part2(_input_):
    cards = _input_.splitlines()

    card_stack = [1] * len(cards)

    for index, line in enumerate(cards):
        groups = re.search(r"Card\s+\d+: ([\d\s]+)\| ([\d\s]+)", line)
        winners = list(map(int, groups.group(1).split()))
        numbers = list(map(int, groups.group(2).split()))

        matches = 0
        for winner in winners:
            if winner in numbers:
                matches += 1

        for i in range(matches):
            ind = index + i + 1
            if ind < len(card_stack):
                card_stack[ind] += card_stack[index] * 1

    return sum(card_stack)


################################################################################

import unittest
import utils


class TestCase(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(13, part1(utils.read("inputs/day4.p1.txt")))
        self.assertEqual(28750, part1(utils.read("inputs/day4.txt")))

    def test_part2(self):
        self.assertEqual(30, part2(utils.read("inputs/day4.p1.txt")))
        self.assertEqual(10212704, part2(utils.read("inputs/day4.txt")))


if __name__ == '__main__':
    unittest.main()
