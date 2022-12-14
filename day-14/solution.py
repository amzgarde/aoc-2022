#!/usr/bin/env python3


def get_input(version):
    filename = "input.txt"
    if version == "test":
        filename = "test-input.txt"
    print(f"Using {filename}")
    with open(filename) as reader:
        return reader.read().splitlines()


def print_cavern(cavern, version):
    with open(f"result-{version}.txt", "w") as append:
        print("=============", file=append)
        message = f"{'I ': <2}"
        for col in range(len(cavern[0])):
            message += str(col % 10)
        print(message, file=append)
        for index, each in enumerate(cavern):
            print(f"{index: <2} {''.join(each)}", file=append)


def create_formation(input):
    left = 1000
    right = 0
    down = 0
    formation = []
    for rocks in input:
        tracing = rocks.split(" -> ")

        tracing = [
            [int(each.split(",")[0]), int(each.split(",")[1])] for each in tracing
        ]
        formation.append(tracing)
        for coord in tracing:
            if coord[0] < left:
                left = coord[0]
            if coord[0] > right:
                right = coord[0]
            if coord[1] > down:
                down = coord[1]
    size = right - left + 1

    print(left)

    cavern = []
    d = 0
    for depth in range(down + 1):
        cavern.append(["."] * size)
        d += 1

    for trace in formation:
        for index in range(1, len(trace)):
            rock1 = trace[index - 1]
            rock2 = trace[index]
            if rock1[0] == rock2[0]:
                x = rock1[0] - left
                y = rock1[1]
                while y <= rock2[1]:
                    cavern[y][x] = "#"
                    y += 1
            if rock1[1] == rock2[1]:
                x = rock1[0] - left
                y = rock1[1]
                dest_x = rock2[0] - left

                if x - dest_x > 0:
                    while x >= dest_x:
                        cavern[y][x] = "#"
                        x -= 1
                elif x - dest_x < 0:
                    while x <= dest_x:
                        cavern[y][x] = "#"
                        x += 1
    return cavern, left


def falling(formation, starting):
    row = starting[0]
    col = starting[1]
    rest = False

    while not rest:

        if col == -1 or col == len(formation[0]) - 1 or row == len(formation) - 1:
            print(formation[row][col - 1])
            print(row, col)
            return formation, True

        if formation[row + 1][col] == ".":
            row += 1
        elif formation[row + 1][col - 1] == ".":
            row += 1
            col -= 1
        elif formation[row + 1][col + 1] == ".":
            row += 1
            col += 1
        else:
            formation[row][col] = "o"
            rest = True
    return formation, False


def main(version="real"):
    input = get_input(version)

    formation, offset = create_formation(input)
    print_cavern(formation, version)
    print("rows = ", len(formation), "cols = ", len(formation[0]))
    starting = [0, 500 - offset]

    safe = True
    sand = 0
    while safe:

        formation, found = falling(formation, starting)
        print_cavern(formation, version)

        if found:
            safe = False
        else:
            sand += 1

    print(sand)


main("test")
main()
