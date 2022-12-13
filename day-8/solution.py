#!/usr/bin/env python3


def get_input(version):
    filename = "input.txt"
    message = "Using real data"
    if version == "test":
        message = "Using test data"
        filename = "test-input.txt"
    print(message)
    with open(filename) as reader:
        return reader.read()


def create_grid(input):
    visible = []
    grid = []
    rows = input.splitlines()
    for row in rows:
        grid.append([*row])
        visible.append([True] * len(row))
    return grid, visible


def is_visible(height, previous):
    if not previous:
        return True
    return height > max(previous)


def compare(grid, visible):
    row_visible = []
    row_visible.append(visible[0])

    for row in grid[1:-1]:
        left = []
        right = []
        forward_row = []
        backward_row = []
        for forward in range(0, len(row)):
            backward_index = len(row) - 1 - forward
            forward_row.append(is_visible(row[forward], left))
            backward_row.append(is_visible(row[backward_index], right))
            left.append(row[forward])
            right.append(row[backward_index])

        backward_row.reverse()
        merged_row = [
            forward_row[i] or backward_row[i] for i in range(len(forward_row))
        ]

        row_visible.append(merged_row)

    row_visible.append(visible[-1])

    return row_visible


def transpose(matrix):
    transposed_matrix = []
    for col in range(0, len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        transposed_matrix.append(new_row)
    return transposed_matrix


def pp(grid):
    for row in grid:
        print(row)


def get_count(col, index, group, reverse=False):
    if not group:
        return 0
    if is_visible(col, group):
        return len(group)
    else:
        trees = 0

        if reverse:
            group.reverse()
        for each in group:
            if each < col:
                trees += 1
            else:
                return trees + 1


def main(version=None):
    input = get_input(version)
    grid, visible = create_grid(input)

    row_visible = compare(grid, visible)
    col_visible = compare(transpose(grid), transpose(visible))
    col_visible = transpose(col_visible)

    visible_count = 0
    final_visibility = []
    for index in range(len(row_visible)):
        row = [
            row_visible[index][i] or col_visible[index][i]
            for i in range(len(row_visible[index]))
        ]
        final_visibility.append(row)
        for each in row:
            if each:
                visible_count += 1

    print("part one")
    print(visible_count)
    print("part two")
    inverted_grid = transpose(grid)

    highest_score = 0

    for ri, row in enumerate(grid):
        for ci, col in enumerate(row):
            left_group = row[0:ci]
            right_group = row[ci + 1 : len(row)]
            left = get_count(col, ci, left_group, True)
            right = get_count(col, ci, right_group)

            inverted_row = inverted_grid[ci]
            up_group = inverted_row[0:ri]
            down_group = inverted_row[ri + 1 : len(inverted_row)]

            up = get_count(col, ci, up_group, True)
            down = get_count(col, ci, down_group)

            score = left * right * up * down
            if score > highest_score:
                highest_score = score
    print(highest_score)


main("test")
main()
