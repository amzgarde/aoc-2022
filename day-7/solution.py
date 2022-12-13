#!/usr/bin/env python3

# find all of the directories with a total size of at most 100000


import re


def input(filename):
    with open(filename) as reader:
        return reader.read().splitlines()


def get_totals(cmds):
    total = {}
    location = []
    for cmd in cmds:
        change_dir = "$ cd "
        ls = "$ ls"
        dir = "dir"
        if cmd.startswith(change_dir):
            folder = cmd.replace(change_dir, "")
            if folder == "..":
                location.pop()
                continue
            location.append(folder)
            if folder not in total:
                total[folder] = 0
            continue

        if cmd.startswith(ls) or cmd.startswith(dir):
            continue

        size = re.findall(r"\d+", cmd)[0]
        for loc in location:
            total[loc] += int(size)

    return total


def main(filename, most):
    print(f"Using {filename}")

    cmds = input(filename)
    total = get_totals(cmds)

    most_total = 0
    mosts = []
    total_size = 0
    for each in total:
        if total[each] <= most:
            most_total += total[each]
            mosts.append(total[each])
        total_size += total[each]

    print(mosts)
    print(len(mosts))
    print(total_size)
    return most_total


filename = "test-input.txt"
most = 100000
total = main(filename, most)
print(total)
print(total == 95437)

filename = "input.txt"
print(main(filename, most))
