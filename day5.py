import re


def part1(_input_):
    groups = re.search(r"seeds: ([\d\s]+?)\n\nseed-to-soil map:\n([\d\s\n]+?)\n\nsoil-to-fertilizer map:\n([\d\s\n]+?)\n\nfertilizer-to-water map:\n([\d\s\n]+?)\n\nwater-to-light map:\n([\d\s\n]+?)\n\nlight-to-temperature map:\n([\d\s\n]+?)\n\ntemperature-to-humidity map:\n([\d\s\n]+?)\n\nhumidity-to-location map:\n([\d\s\n]+)", _input_)

    data = groups.groups()
    seeds = list(map(int, data[0].split()))

    maps = []
    for i in range(1, len(data)):
        maps.append(list(map(lambda x: list(map(int, x.split())), data[i].split("\n"))))

    result = None
    for seed in seeds:
        current = seed
        for m in maps:
            for destination, source, length in m:
                if current >= source and current < source + length:
                    diff = current - source
                    current = destination + diff
                    break
        if not result or current < result:
            result = current

    return result


def part2(_input_):
    groups = re.search(r"seeds: ([\d\s]+?)\n\nseed-to-soil map:\n([\d\s\n]+?)\n\nsoil-to-fertilizer map:\n([\d\s\n]+?)\n\nfertilizer-to-water map:\n([\d\s\n]+?)\n\nwater-to-light map:\n([\d\s\n]+?)\n\nlight-to-temperature map:\n([\d\s\n]+?)\n\ntemperature-to-humidity map:\n([\d\s\n]+?)\n\nhumidity-to-location map:\n([\d\s\n]+)", _input_)

    data = groups.groups()
    seed_ranges = list(map(int, data[0].split()))

    seeds = []
    for i in range(0, len(seed_ranges), 2):
        start = seed_ranges[i]
        length = seed_ranges[i + 1]
        seeds.append([start, length])
    seeds.sort(key=lambda x: x[1])

    maps = []
    for i in range(1, len(data)):
        m = list(map(lambda x: list(map(int, x.split())), data[i].split("\n")))
        m.sort(key=lambda x: x[1])
        maps.append(m)

    result = None
    for i, m in enumerate(maps):
        result = []
        for a_start, a_length in seeds:
            a_end = a_start + a_length

            segments = []

            current_start = a_start
            remaining_length = a_length

            for d, b_start, b_length in m:
                b_end = b_start + b_length

                if current_start >= a_end or a_end <= b_start:
                    continue

                if current_start < b_start:
                    segment_length = min(remaining_length, b_start - current_start)
                    segments.append((current_start, segment_length))
                    current_start += segment_length
                    remaining_length -= segment_length

                if current_start < b_end:
                    segment_length = min(remaining_length, b_end - current_start)
                    segments.append((current_start + (d - b_start), segment_length))
                    current_start += segment_length
                    remaining_length -= segment_length

            if remaining_length > 0:
                segments.append((current_start, remaining_length))

            result.extend(segments)

        result = sorted(result, key=lambda x: x[0])
        seeds = result

    return result[0][0] if result and result[0] else None


################################################################################

import unittest
import utils


class TestCase(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(35, part1(utils.read("inputs/day5.p1.txt")), "Fails on the example input")
        self.assertEqual(382895070, part1(utils.read("inputs/day5.txt")), "Fails on the real input")

    def test_part2(self):
        self.assertEqual(46, part2(utils.read("inputs/day5.p1.txt")), "Fails on the example input")
        self.assertEqual(17729182, part2(utils.read("inputs/day5.txt")), "Fails on the real input")


if __name__ == '__main__':
    unittest.main()
