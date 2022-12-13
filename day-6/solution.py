from collections import deque

with open("test-inputs.txt") as reader:
    tests = reader.read().splitlines()


def process(input, count):
    comm = set()
    marker = 0
    while len(comm) <= count:
        comm.add(input[marker])
        marker += 1
    return marker - 1


def other(string, count):
    stack = deque(string[0:count])

    for i in range(count, len(string)):
        if len(set(stack)) == count:
            print(i)
            break

        stack.popleft()
        stack.append(string[i])


print("==== part 1 ====")

print("test")
for test in tests:
    """
    7,5,6,10,11
    """

    print(process(test, 4))
    print(other(test, 4))

print("real")

with open("input.txt") as reader:
    input = reader.read().strip()

print(process(input, 4))
print(other(input, 4))
print("=== part 2 ====")
print(other(input, 14))
