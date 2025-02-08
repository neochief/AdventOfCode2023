import re


def part1(_input_):
    red = 12
    green = 13
    blue = 14
    result = 0
    for line in _input_.splitlines():
        game_id = int(re.search(r'Game (\d+):', line).group(1))
        games = line.split(':')[1].split(';')
        try:
            for game in games:
                r = int(m.group(1)) if (m := re.search(r'(\d+) red', game)) else 0
                g = int(m.group(1)) if (m := re.search(r'(\d+) green', game)) else 0
                b = int(m.group(1)) if (m := re.search(r'(\d+) blue', game)) else 0

                if r > red or g > green or b > blue:
                    raise StopIteration

            result += game_id

        except StopIteration:
            pass

    return result


def part2(_input_):
    result = 0
    for line in _input_.splitlines():
        games = line.split(':')[1].split(';')
        red, green, blue = 0, 0, 0
        for game in games:
            r = int(m.group(1)) if (m := re.search(r'(\d+) red', game)) else 0
            g = int(m.group(1)) if (m := re.search(r'(\d+) green', game)) else 0
            b = int(m.group(1)) if (m := re.search(r'(\d+) blue', game)) else 0
            if r > red:
                red = r
            if g > green:
                green = g
            if b > blue:
                blue = b
        result += red * green * blue
    return result


################################################################################

import unittest
import utils


class TestCase(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(8, part1(utils.read("inputs/day2.p1.txt")), "Fails on the example input")
        self.assertEqual(2149, part1(utils.read("inputs/day2.txt")), "Fails on the real input")

    def test_part2(self):
        self.assertEqual(2286, part2(utils.read("inputs/day2.p2.txt")), "Fails on the example input")
        self.assertEqual(71274, part2(utils.read("inputs/day2.txt")), "Fails on the real input")


if __name__ == '__main__':
    unittest.main()
