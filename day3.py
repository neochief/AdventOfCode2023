def part1(_input_):
    map = {}
    for y, line in enumerate(_input_.splitlines()):
        map[y] = list(line)

    def has_symbol_around(y, sx, l):
        def is_symbol(c):
            return not c.isdigit() and c != '.'

        for x in range(sx, sx + l):
            if x - 1 >= 0 and is_symbol(map[y][x - 1]):
                return True
            if x + 1 < len(map[y]) and is_symbol(map[y][x + 1]):
                return True
            if y - 1 >= 0 and is_symbol(map[y - 1][x]):
                return True
            if y + 1 < len(map) and is_symbol(map[y + 1][x]):
                return True
            if x - 1 >= 0 and y - 1 >= 0 and is_symbol(map[y - 1][x - 1]):
                return True
            if x + 1 < len(map[y]) and y - 1 >= 0 and is_symbol(map[y - 1][x + 1]):
                return True
            if x - 1 >= 0 and y + 1 < len(map) and is_symbol(map[y + 1][x - 1]):
                return True
            if x + 1 < len(map[y]) and y + 1 < len(map) and is_symbol(map[y + 1][x + 1]):
                return True

        return False

    result = 0
    for y, line in map.items():
        x = 0
        num = ''
        while x < len(line):
            c = line[x]

            xs = x
            if c.isdigit():
                num = c
                while x + 1 < len(line):
                    x += 1
                    cc = line[x]
                    if cc.isdigit():
                        num += cc
                    else:
                        break

            if num and has_symbol_around(y, xs, len(num)):
                result += int(num)

            num = ''
            x += 1

    return result


def part2(_input_):
    map = {}
    for y, line in enumerate(_input_.splitlines()):
        map[y] = list(line)

    def has_symbol_around(y, sx, l, symbol=None):
        def is_symbol(c):
            return (symbol and c == symbol) or (not symbol and not c.isdigit() and c != '.')

        coords = set()
        for x in range(sx, sx + l):
            if x - 1 >= 0 and is_symbol(map[y][x - 1]):
                coords.add((y, x - 1))
            if x + 1 < len(map[y]) and is_symbol(map[y][x + 1]):
                coords.add((y, x + 1))
            if y - 1 >= 0 and is_symbol(map[y - 1][x]):
                coords.add((y - 1, x))
            if y + 1 < len(map) and is_symbol(map[y + 1][x]):
                coords.add((y + 1, x))
            if x - 1 >= 0 and y - 1 >= 0 and is_symbol(map[y - 1][x - 1]):
                coords.add((y - 1, x - 1))
            if x + 1 < len(map[y]) and y - 1 >= 0 and is_symbol(map[y - 1][x + 1]):
                coords.add((y - 1, x + 1))
            if x - 1 >= 0 and y + 1 < len(map) and is_symbol(map[y + 1][x - 1]):
                coords.add((y + 1, x - 1))
            if x + 1 < len(map[y]) and y + 1 < len(map) and is_symbol(map[y + 1][x + 1]):
                coords.add((y + 1, x + 1))

        return coords

    result = 0
    gears = {}
    for y, line in map.items():
        x = 0
        num = ''
        while x < len(line):
            c = line[x]

            xs = x
            if c.isdigit():
                num = c
                while x + 1 < len(line):
                    x += 1
                    cc = line[x]
                    if cc.isdigit():
                        num += cc
                    else:
                        break

            if num:
                attached_gears = has_symbol_around(y, xs, len(num), '*')
                for coords in attached_gears:
                    gears.setdefault(coords, []).append(num)

            num = ''
            x += 1

    for gears in gears.values():
        if len(gears) == 2:
            result += int(gears[0]) * int(gears[1])

    return result


################################################################################

import unittest
import utils


class TestCase(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(4361, part1(utils.read("inputs/day3.p1.txt")), "Fails on the example input")
        self.assertEqual(532428, part1(utils.read("inputs/day3.txt")), "Fails on the real input")

    def test_part2(self):
        self.assertEqual(467835, part2(utils.read("inputs/day3.p2.txt")), "Fails on the example input")
        self.assertEqual(84051670, part2(utils.read("inputs/day3.txt")), "Fails on the real input")


if __name__ == '__main__':
    unittest.main()
