#!/usr/bin/env python3


def convert(you):
    convert = {"X": "A", "Y": "B", "Z": "C"}
    return convert[you]


def winner_score(game):
    draw = ["AA", "BB", "CC"]
    if game in draw:
        return 3

    combo_opp_win = ["AC", "BA", "CB"]

    if game in combo_opp_win:
        return 0

    return 6


def choice_score(you):
    choice = {"A": 1, "B": 2, "C": 3}

    return choice[you]


def read_input(filename):
    with open(filename) as reader:
        games = reader.read().replace(" ", "").splitlines()

        return games


def total_score(games):
    total = 0
    for game in games:
        you = convert(game[1])
        your_score = choice_score(you)
        new_game = f"{game[0]}{you}"
        winning_score = winner_score(new_game)
        total += your_score + winning_score
    return total


def choose(opp, strategy):
    if strategy == "X":
        lose = ["AC", "BA", "CB"]
        for each in lose:
            if opp == each[0]:
                return each
    if strategy == "Y":
        draw = ["AA", "BB", "CC"]
        for each in draw:
            if opp == each[0]:
                return each
    if strategy == "Z":
        win = ["AB", "BC", "CA"]
        for each in win:
            if opp == each[0]:
                return each


def new_total(games):
    total = 0
    for game in games:
        round = choose(game[0], game[1])
        your_score = choice_score(round[1])
        round_score = winner_score(round)
        total += your_score + round_score
    return total


games = read_input("input.txt")
total = total_score(games)
print("Total score")
print(total)

new_total = new_total(games)
print("Part two - total")
print(new_total)
