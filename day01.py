# https://adventofcode.com/2024/day/1

def part1(lefts, rights):
    return sum([abs(int(i) - int(j)) for i,j in zip(sorted(lefts), sorted(rights))]) # diff sum

def part2(lefts, rights):
    leftCounts, rightCounts = {}, {}
    for i in range(len(lefts)):
        leftNum, rightNum = lefts[i], rights[i]
        leftCounts[leftNum] = leftCounts.get(leftNum, 0) + 1
        rightCounts[rightNum] = rightCounts.get(rightNum, 0) + 1
    return sum([int(n) * leftCounts.get(n,0) * rightCounts.get(n,0) for n in list(leftCounts)])

def processInput():
    with open("day01.txt") as file:
        return list(zip(*[line.strip().split() for line in file]))

def main():
    inputs = processInput()
    print(f"Part one answer: {part1(*inputs)}")
    print(f"Part two answer: {part2(*inputs)}")

main()