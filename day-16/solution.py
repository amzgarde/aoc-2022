#!/usr/bin/env python3


import re


def get_input(version):
    filename = "input.txt"
    if version == "test":
        filename = "test-input.txt"
    print(f"Using {filename}")
    with open(filename) as reader:
        return reader.read()


def parse_path(input):
    flow_pattern = r"\d+"
    valve_pattern = r"([A-Z]{2})"
    parsed_input = {}
    to_visit = []
    for line in input.splitlines():
        flow = re.findall(flow_pattern, line)[0]

        valves = re.findall(valve_pattern, line)
        source = valves.pop(0)

        parsed_input[source] = {"flow": int(flow), "targets": valves}
        to_visit.append(source)

    return parsed_input, to_visit


def build_paths(input):
    pressure = []
    tt = 0
    visited = []
    previous = "AA"
    curr = "AA"
    while tt < 30:
        if curr not in visited:
            if input[curr]["flow"] != 0:
                tt += 1
                pressure.append((input[curr]["flow"], tt))
                input[curr]["flow"] = 0
            visited.append(curr)
        for target in input[curr]["targets"]:
            if target not in visited:
                input[curr]["previous"] = curr
                curr = target
                
                continue
        for target in input[curr][previous]


def main(version=None):
    input = get_input(version)
    input, to_visit = parse_path(input)

    paths = build_paths(
        input,
        to_visit,
    )

    # if flow != 0 -> open
    # move to next point

    # 30 minutes to escape
    # network of values
    # value flow rate if it were opened in pressure per minute (puzzle input)
    # Elephants at AA
    # one minute to open a single value
    # one minute to follow any tunnel to another valve

    # All valves are closed
    # Start at AA
    # release pressure is goal
    # pressure * remaining time == total eventual pressure


main("test")
# main()
