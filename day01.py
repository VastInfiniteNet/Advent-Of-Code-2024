# https://adventofcode.com/2024/day/1

def part1():
    left, right, total = [], [], 0
    with open("day01.txt") as file:
        for line in file:
            line = line.strip().split()
            left.append(int(line[0]))
            right.append(int(line[1]))
    left.sort()
    right.sort()

    while left and right:
        total += abs(left.pop() - right.pop())

    print(total)

def part2():
    left, right, total = {}, {}, 0
    with open("day01.txt") as file:
        for line in file:
            line = line.strip().split()
            leftNum, rightNum = line[0], line[1]
            if leftNum in left:
                left[leftNum] += 1
            else:
                left[leftNum] = 1
            if rightNum in right:
                right[rightNum] += 1
            else:
                right[rightNum] = 1
    for n in list(left):
        if n in right:
            total += int(n) * left[n] * right[n]

    print(total)


#part1()
part2()