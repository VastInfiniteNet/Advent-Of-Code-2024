from collections import defaultdict
import time
startTime = time.time_ns()
antennas = defaultdict(list)
y, x = 0, 0
antinodes = set()
with open("day08.txt") as file:
    for line in file:
        y = 0
        for char in line.rstrip():
            if char != '.':
                antennas[char].append((x, y))
            y += 1
        x += 1
width = x
height = y

def countAntinodes(countFunc):
    for spots in antennas.values():
        spotCount = len(spots)
        for i in range(spotCount - 1):
            for j in range(i+1, spotCount):
               countFunc(spots[i], spots[j]) 
    return len(antinodes)

def addAntinodes(a, b):
    yDiff, xDiff = (a[0] - b[0]), (a[1] - b[1])
    cand1 = (a[0] + yDiff, a[1] + xDiff) 
    cand2 = (a[0] - yDiff, a[1] - xDiff)

    if cand1 == b: # move again!
        cand1 = (cand1[0] + yDiff, cand1[1] + xDiff)
    elif cand2 == b: #move again!
        cand2 = (cand2[0] - yDiff, cand2[1] - xDiff)
    if -1 < cand1[1] < width and -1 < cand1[0] < height:
        antinodes.add(cand1)
    if -1 < cand2[1] < width and -1 < cand2[0] < height:
        antinodes.add(cand2)

def addHarmonicAntinodes(a, b):
    yDiff, xDiff = (a[0] - b[0]), (a[1] - b[1])
    cand1 = (a[0] + yDiff, a[1] + xDiff) 
    cand2 = (a[0] - yDiff, a[1] - xDiff)
    antinodes.add(a)
    antinodes.add(b)

    while -1 < cand1[1] < width and -1 < cand1[0] < height:
        antinodes.add(cand1)
        cand1 = (cand1[0] + yDiff, cand1[1] + xDiff)

    while -1 < cand2[1] < width and -1 < cand2[0] < height:
        antinodes.add(cand2)
        cand2 = (cand2[0] - yDiff, cand2[1] - xDiff)

print(f'Part 1: {countAntinodes(addAntinodes)}')
print(f'Part 2: {countAntinodes(addHarmonicAntinodes)}')
print(f'Total Elapsed: {time.time_ns() - startTime}')