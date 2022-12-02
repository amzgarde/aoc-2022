#!/usr/bin/env python3


def get_input():
    with open("input.txt") as reader:
        groups = reader.read().split("\n\n")

        return groups


def find_max_cals(groups):

    max_cals = 0

    for each in groups:
        lines = each.splitlines()

        each_cal = 0

        for line in lines:
            each_cal += int(line)

        if each_cal > max_cals:
            max_cals = each_cal

    return max_cals


def find_top_three(groups):
    cals = []

    for each in groups:
        lines = each.splitlines()

        each_cal = 0

        for line in lines:
            each_cal += int(line)

        # Add highest to the top of the list
        cals.append(each_cal)

    top_three = sorted(cals)[-3:]

    return sum(top_three)


# Part one - most cals
groups = get_input()
print("Max Calories")
print(find_max_cals(groups))

# Part two - top three cals
print("Top three calories")
print(find_top_three(groups))
