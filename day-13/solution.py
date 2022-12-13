#!/usr/bin/env python3


import ast
import functools


def get_input(version):
    filename = "input.txt"
    if version == "test":
        filename = "test-input.txt"
    print(f"Using {filename}")
    with open(filename) as reader:
        return reader.read()


def compare(left, right):
    left = ast.literal_eval(left)
    right = ast.literal_eval(right)
    result = compare_list(right, left)
    return result


def compare_list(left, right):
    result = 0
    while result == 0 and len(left) and len(right):
        l_compare = left.pop(0)
        r_compare = right.pop(0)

        if isinstance(l_compare, int) and isinstance(r_compare, int):
            if l_compare < r_compare:
                return 1
            if l_compare > r_compare:
                return -1
        elif isinstance(l_compare, list) and isinstance(r_compare, list):
            result = compare_list(l_compare, r_compare)

        elif isinstance(l_compare, list) and isinstance(r_compare, int):
            result = compare_list(l_compare, [r_compare])

        elif isinstance(l_compare, int) and isinstance(r_compare, list):
            result = compare_list([l_compare], r_compare)

    if result == 0:
        if len(left) < len(right):
            result = 1
        elif len(left) > len(right):
            result = -1

    return result


def main(version=None):
    input = get_input(version)

    pairs = input.split("\n\n")

    sum = 0
    count = 0
    for index, pair in enumerate(pairs):
        pair = pair.split("\n")

        left = ast.literal_eval(pair[0])
        right = ast.literal_eval(pair[1])

        result = compare_list(left, right)
        if result == 1:
            sum += index + 1
            count += 1 * result

    print("Sum =", sum)

    added = ["[[2]]", "[[6]]"]
    input = [line for line in input.split("\n") if line.strip() != ""] + added

    part2 = sorted(input, key=functools.cmp_to_key(compare))

    locations = 1
    for index, each in enumerate(part2):
        if each in added:
            locations *= index + 1

    print("Decoder key =", locations)


main("test")
main()
