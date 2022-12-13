#!/usr/bin/env python3

import re


def get_input(version):
    filename = "input.txt"
    if version == "test":
        filename = "test-input.txt"
    print(f"Using {filename}")
    with open(filename) as reader:
        return reader.read().splitlines()


def move_section(h, t):
    if abs(h[0] - t[0]) < 2 and abs(h[1] - t[1]) < 2:
        return t

    xdiff = h[0] - t[0]
    ydiff = h[1] - t[1]

    if xdiff < 0:
        t[0] -= 1
    elif xdiff > 0:
        t[0] += 1
    if ydiff < 0:
        t[1] -= 1
    elif ydiff > 0:
        t[1] += 1

    return t


def update_rope(h, rope):
    previous = h
    new_rope = []
    for knot in rope:
        new_rope.append(move_section(previous, knot))
        previous = knot

    return new_rope


def main(version=None, longer=False):
    moves = get_input(version)

    h_pos = [0, 0]
    t_pos = [0, 0]
    rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    all_t = set()
    all_t.add(tuple(t_pos))

    for move in moves:
        num = re.findall(r"\d+", move)[0]
        if move.startswith("R"):
            for each in range(int(num)):
                h_pos[0] += 1
                new_pos = h_pos
                if longer:
                    rope = update_rope(h_pos, rope)
                    new_pos = rope[-1]
        if move.startswith("L"):
            for each in range(int(num)):
                h_pos[0] -= 1
                new_pos = h_pos
                if longer:
                    rope = update_rope(h_pos, rope)
                    new_pos = rope[-1]
        if move.startswith("U"):
            for each in range(int(num)):
                h_pos[1] += 1
                new_pos = h_pos
                if longer:
                    rope = update_rope(h_pos, rope)
                    new_pos = rope[-1]
        if move.startswith("D"):
            for each in range(int(num)):
                h_pos[1] -= 1
                new_pos = h_pos
                if longer:
                    rope = update_rope(h_pos, rope)
                    new_pos = rope[-1]

        t_pos = move_section(new_pos, t_pos)
        all_t.add(tuple(t_pos))

    print(len(all_t))


main("test")
main("test", True)
main()
main("real", True)
