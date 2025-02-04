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
        self.assertEqual(0, part1(utils.read("inputs/day2.p1.txt")))

    #def test_part2(self):
    #    self.assertEqual(0, part2(utils.read("inputs/day2.p2.txt")))

if __name__ == '__main__':
    unittest.main()
