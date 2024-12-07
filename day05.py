# https://adventofcode.com/2024/day/5
from functools import cmp_to_key
pageRules, pageUpdates = {}, []

def part1():
    total = 0
    for update in pageUpdates:
        valid = True
        for i in range(1, len(update)):
            if update[i] not in pageRules.get(update[i-1], []):
                valid = False
                break
        if valid:
            total += update[len(update)//2]
    return total

def updatePageCmpr(page1, page2):
    if page2 in pageRules.get(page1, []):
        return -1
    if page1 in pageRules.get(page2, []):
        return 1

def part2():
    total = 0
    for update in pageUpdates:
        for i in range(1, len(update)):
            if update[i] not in pageRules.get(update[i-1], []):
                update.sort(key=cmp_to_key(updatePageCmpr))
                total += update[len(update)//2]
                break
    return total

def processInput():
    with open("day05.txt") as file:
        line = file.readline()
        while line != "": # page rules parsing
            if line == '\n':
                break
            line = list(map(int, line.split('|')))
            pageRules[line[0]] = pageRules.get(line[0], []) + [line[1]]
            line = file.readline()
        line = file.readline() # skip blank line
        while line != "": # page updates parsing
            pageUpdates.append(list(map(int, line.split(','))))
            line = file.readline()

processInput()
print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")