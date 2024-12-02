# https://adventofcode.com/2024/day/1

def part1(lefts, rights):
    total = 0
    leftNums = sorted(lefts)
    rightNums = sorted(rights)
    for i in range(len(leftNums)):
        total += abs(int(leftNums[i]) - int(rightNums[i]))
    return total

def part2(lefts, rights):
    leftCounts, rightCounts, total = {}, {}, 0
    for i in range(len(lefts)):
        leftNum, rightNum = lefts[i], rights[i]
        if leftNum in leftCounts:
            leftCounts[leftNum] += 1
        else:
            leftCounts[leftNum] = 1
        if rightNum in rightCounts:
            rightCounts[rightNum] += 1
        else:
            rightCounts[rightNum] = 1
    for n in list(leftCounts):
        if n in rightCounts:
            total += int(n) * leftCounts[n] * rightCounts[n]
    return total

def processInput():
    left, right = [], []
    with open("day01.txt") as file:
        for line in file:
            leftString, rightString = line.strip().split()
            left.append(leftString)
            right.append(rightString)
    return (left, right)

def main():
    inputs = processInput()

    print(f"Part one answer: {part1(*inputs)}")
    print(f"Part two answer: {part2(*inputs)}")


main()