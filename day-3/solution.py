import string

priority = dict(zip(string.ascii_lowercase, range(1, 27)))

priority.update(dict(zip(string.ascii_uppercase, range(27, 53))))

with open("input.txt") as reader:
    lines = reader.read().splitlines()

priority_num = 0
for line in lines:
    half1 = set(line[: len(line) // 2])
    half2 = set(line[len(line) // 2 :])
    common = list(half1 & half2)[0]

    priority_num += priority[common]
print("part 1")
print(priority_num)

groups = zip(*(iter(lines),) * 3)

group_priority = 0
for group in groups:
    a = set(group[0])
    b = set(group[1])
    c = set(group[2])
    common = list(a & b & c)[0]

    group_priority += priority[common]

print("part 2")
print(group_priority)
