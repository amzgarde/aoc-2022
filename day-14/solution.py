#!/usr/bin/env python3


import os


def get_input(version):
    filename = "input.txt"
    if version == "test":
        filename = "test-input.txt"
    print(f"Using {filename}")
    with open(filename) as reader:
        return reader.read().splitlines()


def print_cavern(cavern, version, file = True):
    folder = "results"
    if not os.path.exists(folder):
        os.mkdir(folder)
        
    with open(f"{folder}/result-{version}.txt", "w") as append:
        message = f"{'I ': <3}"
        for col in range(len(cavern[0])):
            message += str(col % 10)
        if file:
            print(message, file=append)
        else:
            print(message)
        for index, each in enumerate(cavern):
            if file:
                print(f"{index: <2} {''.join(each)}", file=append)
            else:
                print(f"{index: <2} {''.join(each)}")


def create_formation(input):
    x = []
    y = []
    formation = []
    for rocks in input:
        tracing = [
            [int(each.split(",")[0]), int(each.split(",")[1])] for each in rocks.split(" -> ")
        ]
        formation.append(tracing)
        
        for coord in tracing:
            x.append(coord[0])
            y.append(coord[1])

    offset = min(x)
    size = max(x) - offset + 1

    cavern = [['.'] * size for _ in range(max(y) + 1)]
    
    for trace in formation:
        for index in range(1, len(trace)):
            source = trace[index - 1]
            dest = trace[index]
            if source[0] == dest[0]:
                row = source[0] - offset
                
                start = min([source[1], dest[1]])
                end = max([source[1], dest[1]])
                
                for point in range(start, end):
                    cavern[point][row] = "#"
            if source[1] == dest[1]:
                col = source[1]
                
                start = min([source[0], dest[0]])
                end = max([source[0], dest[0]])
                
                for point in range(start, end + 1):
                    point -= offset
                    cavern[col][point] = "#"
    return cavern, offset


def falling(formation, starting):
    row = starting[0]
    col = starting[1]
    rest = False

    while not rest:
        if row == len(formation) - 1:
            return formation, True
        elif formation[row + 1][col] == ".":
            row += 1
        elif col == 0:
            return formation, True
        elif formation[row + 1][col - 1] == ".":
            row += 1
            col -= 1
        elif col == len(formation[0]) - 1:
            return formation, True
        elif formation[row + 1][col + 1] == ".":
            row += 1
            col += 1
        else:
            formation[row][col] = "o"
            rest = True
    return formation, False

def update_formation(formation, location):
    new_formation = []
    for index, each_row in enumerate(formation):
        if index == len(formation) - 1:
            each_row.insert(location, "#")
        else:
            each_row.insert(location, ".")
        new_formation.append(each_row)
    return new_formation

def falling_pt2(formation, starting):
    row = starting[0]
    col = starting[1]
    rest = False

    while not rest:
        if col == 0:
            col += 1
            formation = update_formation(formation, 0)
            starting[1] += 1
        elif col == len(formation[0]) - 1:
            formation = update_formation(formation, len(formation[0]))

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
            if [row, col] == starting:
                return formation, starting, True
            rest = True
    return formation, starting, False


def main(version="real"):
    input = get_input(version)

    cavern, offset = create_formation(input)
    starting = [0, 500 - offset]

    safe = True
    formation = cavern
    while safe:

        formation, found = falling(formation, starting)
        print_cavern(formation, version)

        if found:
            safe = False

    count_o = ("".join([item for sublist in formation for item in sublist]).count("o"))
    
    print("Part 1:", count_o)

    safe = True
    formation = cavern
    formation.append(["."]*len(formation[0]))
    formation.append(["#"]*len(formation[0]))
    while safe:

        formation, starting, found = falling_pt2(formation, starting)
        print_cavern(formation, f"{version}-pt2")

        if found:
            safe = False

    count_o = ("".join([item for sublist in formation for item in sublist]).count("o"))
    
    print("Part 2:", count_o)


main("test")
main()
