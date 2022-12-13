#!/usr/bin/env python3


import re

test_stack = ["ZN", "MCD", "P"]
real_stack = [
    "SZPDLBFC",
    "NVGPHWB",
    "FWBJG",
    "GJNFLWCS",
    "WJLTPMSH",
    "BCWGFS",
    "HTPMQBW",
    "FSWT",
    "NCR",
]


def create_stack(test=False):
    stack = []
    if test:
        setup = test_stack
    else:
        setup = real_stack
    for ts in setup:
        stack.append(list(map(str, ts)))

    return stack


def get_nums(line):
    return re.findall(r"\d+", line)


stack = create_stack(True)

with open("test-input.txt") as reader:
    moves = reader.read().splitlines()

for move in moves:
    nums = get_nums(move)
    source = int(nums[1]) - 1
    dest = int(nums[2]) - 1

    for step in range(int(nums[0])):
        taken = stack[source].pop()
        stack[dest].append(taken)

result = ""
for each in stack:
    result += each.pop()

print("part 1")
print("test")
print(result)

stack = create_stack()

with open("input.txt") as reader:
    moves = reader.read().splitlines()

for move in moves:
    nums = get_nums(move)
    source = int(nums[1]) - 1
    dest = int(nums[2]) - 1

    for step in range(int(nums[0])):
        taken = stack[source].pop()
        stack[dest].append(taken)

result = ""
for each in stack:
    result += each.pop()

print("real")
print(result)

print("======= part 2 ======")
print("test")

stack = create_stack(True)

with open("test-input.txt") as reader:
    moves = reader.read().splitlines()

for move in moves:
    nums = get_nums(move)
    source = int(nums[1]) - 1
    dest = int(nums[2]) - 1
    to_take = int(nums[0])

    taken = stack[source][-to_take:]
    del stack[source][-to_take:]
    stack[dest] = stack[dest] + taken

result = ""
for each in stack:
    result += each.pop()

print(result)

print("real")

stack = create_stack()

with open("input.txt") as reader:
    moves = reader.read().splitlines()

for move in moves:
    nums = get_nums(move)
    source = int(nums[1]) - 1
    dest = int(nums[2]) - 1
    to_take = int(nums[0])

    taken = stack[source][-to_take:]
    del stack[source][-to_take:]
    stack[dest] = stack[dest] + taken

result = ""
for each in stack:
    result += each.pop()

print(result)
