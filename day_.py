def part1(_input_):
    print(_input_)
    result = 0
    return result


# def part2(_input_):
#     print(_input_)
#     result = 0
#     return result


################################################################################

import unittest
import utils


class TestCase(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(0, part1(utils.read("inputs/day.p1.txt")), "Fails on the example input")
        self.assertEqual(0, part1(utils.read("inputs/day.txt")), "Fails on the real input")

    # def test_part2(self):
    #    self.assertEqual(0, part2(utils.read("inputs/day.p2.txt")), "Fails on the example input")
    #    self.assertEqual(0, part2(utils.read("inputs/day.txt")), "Fails on the real input")


if __name__ == '__main__':
    unittest.main()
