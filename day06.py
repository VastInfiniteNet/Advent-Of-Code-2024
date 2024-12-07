"""
BROKEN -- takes WAYYYYYY TOOOOO LOONG!!!!!!
"""

blockers, visited, start = [], set(), ()
width, height = 0, 0
turnCycle = {(-1, 0): (0,1), (0,1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}

with open("day06.txt") as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line.strip()):
            if char == '#':
                blockers.append((y, x))
            elif start == () and char == '^':
                start = (y, x)
        height = y + 1
        width = len(line.strip())

currDir = (-1, 0)
currPos = start
visited.add((currPos, currDir))
touchedBlockers = []
while True:
    currPos = (currPos[0] + currDir[0], currPos[1] + currDir[1]) # keep moving
    if not (-1 < currPos[0] < height) or not (-1 < currPos[1] < width): # off map
        break
    if currPos in blockers: # on a blocker, move back and turn right
        touchedBlockers.append(currPos)
        currPos = (currPos[0] - currDir[0], currPos[1] - currDir[1])
        currDir = turnCycle[currDir]
        continue
    visited.add((currPos, currDir))

print(f'Part one: {len(visited)}')

def isGuardCycle(guardBlocks, blockerPos, blockerDir):
    guardPos, guardDir = start, (-1, 0)
    vistedPos = set((guardPos, guardDir))
    while True:
        guardPos = (guardPos[0] + guardDir[0], guardPos[1] + guardDir[1]) # keep moving
        if not (-1 < guardPos[0] < height) or not (-1 < guardPos[1] < width): # off map
            break
        if guardPos in guardBlocks: # on a blocker, move back and turn right
            guardPos = (guardPos[0] - guardDir[0], guardPos[1] - guardDir[1])
            guardDir = turnCycle[guardDir]
            continue
        if (guardPos, guardDir) in vistedPos: # loop completed
            return True
        vistedPos.add((guardPos, guardDir))
    return False # ran off map, no loop

visited.remove((start, (-1, 0)))
print(touchedBlockers)
cycleSpots = sum([isGuardCycle(blockers + [blockerPos], blockerPos, blockerDir) for (blockerPos, blockerDir) in visited]) 
print(f'Part two: {cycleSpots}')