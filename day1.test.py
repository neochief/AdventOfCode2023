import unittest

from utils import read
from day1 import part1
from day1 import part2

class TestCase(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1(read("inputs/day1.txt")), 52974)

    def test_part2(self):
        self.assertEqual(part2(read("inputs/day1.txt")), 53340)

if __name__ == '__main__':
    unittest.main()
