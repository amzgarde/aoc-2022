#!/usr/bin/env python3


import re
import math

def get_input(version):
  filename = "input.txt"
  if version =="test":
    filename = "test-input.txt"
  print(f"Using {filename}")
  with open(filename) as reader:
    return reader.read()

def convert_op(op):
  if "+" in op:
    type = "+"
    action = "add"
  if "*" in op:
    type = "*"
    action = "mul"
  value = op.split(type)[1].strip()
  if value == "old":
    return (action, "old")
  return (action, (int(value)))
    

def convert(input):
  lines = input.splitlines()
  
  structure = {}
  divisible = []
  
  monkey = -1
  for line in lines:
    line = line.strip()
    if line.startswith("Monkey"):
      monkey += 1
      structure[monkey] = {}
      structure[monkey]["count"] = 0
    if line.startswith("Starting items"):
      values = line.split(":")[1].strip().split(",")
      items = [(int(x)) for x in values]
      structure[monkey]["items"] = items
    if line.startswith("Operation"):
      value = line.split(":")[1].strip()
      op = convert_op(value)
      structure[monkey]["operation"] = op
    if line.startswith("Test"):
      value = re.findall(r'[0-9]+', line)[0]
      structure[monkey]["test"] = {}
      structure[monkey]["test"]["divisible"] = int(value)
      divisible.append(int(value))
    if line.startswith("If true"):
      value = re.findall(r'[0-9]+', line)[0]
      structure[monkey]["test"]["true"] = int(value)
    if line.startswith("If false"):
      value = re.findall(r'[0-9]+', line)[0]
      structure[monkey]["test"]["false"] = int(value)
  return structure, divisible

def preform_op(worry, op):
  incr = op[1]
  if op[1] == "old":
    return pow(worry, 2)
  if op[0] == "add":
    worry += incr
  elif op[0] == "mul":
    worry *= incr
  return worry

def main(version = None, rounds = 20):
  input = get_input(version)
  input, divisible = convert(input)

  mod = math.lcm(*divisible)
  
  for x in range(rounds):
    print(f"======= Round {x} =======")

    for monkey in input:
      items = input[monkey]["items"]
      op = input[monkey]["operation"]
      test = input[monkey]["test"]["divisible"]
      test_true = input[monkey]["test"]["true"]
      test_false = input[monkey]["test"]["false"]
      
      t = []
      f = []
      for item in items:
        worry = preform_op(item, op)

        # worry = math.floor(worry / 3)
        worry = worry % mod
        
        if worry % test == 0:
          t.append((worry))
        else:
          f.append((worry))
      input[test_true]["items"] = input[test_true]["items"] + t
      input[test_false]["items"] = input[test_false]["items"] + f

      input[monkey]["count"] += len(items)
      input[monkey]["items"] = []

  counts = []
  for monkey in input:
    counts.append(input[monkey]["count"])

  sor = sorted(counts)
  monkey_business = sor[-1] * sor[-2]
  print(monkey_business)

main("test", 10000)
main("real", 10000)
