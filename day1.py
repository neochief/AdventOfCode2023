def part1(_input_):
    lines = _input_.splitlines()
    result = 0
    for line in lines:
        first = None
        last = None
        for char in line:
            if char.isdigit():
                if first is None:
                    first = char
                last = char
        if first is not None and last is not None:
            result += int(first + last)
    return result


def part2(_input_):
    lines = _input_.splitlines()
    result = 0

    numberStrings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for line in lines:
        first = None
        last = None
        for index, char in enumerate(line):
            if char.isdigit():
                if first is None:
                    first = char
                last = char
            else:
                for i, numberStr in enumerate(numberStrings):
                    if (index + len(numberStr) <= len(line) and
                            line[index:index + len(numberStr)] == numberStr):
                        if first is None:
                            first = str(i + 1)
                        last = str(i + 1)
                        break

        if first is not None and last is not None:
            result += int(first + last)

    return result


################################################################################

import unittest
import utils


class TestCase(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(142, part1(utils.read("inputs/day1.p1.txt")), "Fails on the example input")
        self.assertEqual(52974, part1(utils.read("inputs/day1.txt")), "Fails on the real input")

    def test_part2(self):
        self.assertEqual(281, part2(utils.read("inputs/day1.p2.txt")), "Fails on the example input")
        self.assertEqual(53340, part2(utils.read("inputs/day1.txt")), "Fails on the real input")


if __name__ == '__main__':
    unittest.main()
