# 13140

import re
import math


def get_input(version):
    filename = "input.txt"
    if version == "test":
        filename = "test-input.txt"
    print(f"using {filename}")
    with open(filename) as reader:
        return reader.read().splitlines()


def part_one(cycle, registry):
    if (cycle + 20) % 40 == 0:
        return cycle * registry
    return 0


def draw(cycle, registry):
    adjust = math.floor(cycle / 40) * 40
    if abs(cycle - 1 - adjust - registry) <= 1:
        return "#"
    return "."


def change_row(cycle, registry, row):
    row += draw(cycle, registry)
    if cycle % 40 == 0:
        print(row)
        return ""
    return row


def main(version=None):
    input = get_input(version)
    cycle = 0
    registry = 1
    sum = 0
    crt = []
    row = ""
    count = 0
    adjust = 0

    for command in input:
        if command == "noop":
            cycle += 1
            sum += part_one(cycle, registry)
            row = change_row(cycle, registry, row)
            continue
        spl = command.split()
        if spl[0] == "addx":
            for x in range(2):
                cycle += 1
                sum += part_one(cycle, registry)
                row = change_row(cycle, registry, row)

            registry += int(spl[1])

    print(sum)


main("test")
main()
