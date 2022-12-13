def make_set(pair):
    a = range(int(pair.split("-")[0]), int(pair.split("-")[1]) + 1)
    return set(list(a))


with open("input.txt") as reader:
    lines = reader.read().splitlines()

subs = 0
overlap = 0
for line in lines:
    pair = line.split(",")
    first = make_set(pair[0])
    second = make_set(pair[1])

    if first.issubset(second) or second.issubset(first):
        subs += 1
    if first.intersection(second):
        overlap += 1

print("part 1")
print(subs)
print("part 2")
print(overlap)
