from collections import deque

def processInput() -> list[list[int]]:
    trailHeads, map = [], []
    x,y = 0,0
    with open("day10.txt") as file:
        for line in file:
            x = 0
            map.append([])
            for char in line.strip():
                map[-1].append(int(char))
                if char == '0':
                    trailHeads.append((y,x))
                x += 1
            y += 1
    return (map, trailHeads)    
    
def graphify(map: list[list[int]], trailHeads: list[tuple[int, int, int]]) -> int:
    totalPeaks = 0
    height, width = len(map), len(map[0])
    for head in trailHeads:
        seenPositions = set()
        queue = deque([[0, head[0], head[1]]])
        seenPositions.add(head)
        while queue:
            altitude, currY, currX = queue.popleft()
            if altitude == 9:
                totalPeaks += 1
                continue
            if currY > 0 and map[currY - 1][currX] == altitude + 1 and (currY - 1, currX) not in seenPositions: # UP
                queue.append([altitude + 1, currY - 1, currX])
                seenPositions.add((currY - 1, currX))
            if currX < width - 1 and map[currY][currX + 1] == altitude + 1 and (currY, currX + 1) not in seenPositions: # RIGHT
                queue.append([altitude + 1, currY, currX + 1])
                seenPositions.add((currY, currX + 1))
            if currY < height - 1 and map[currY + 1][currX] == altitude + 1 and (currY + 1, currX) not in seenPositions: # DOWN
                queue.append([altitude + 1, currY + 1, currX])
                seenPositions.add((currY + 1, currX))
            if currX > 0 and map[currY][currX - 1] == altitude + 1 and (currY, currX - 1) not in seenPositions: #LEFT
                queue.append([altitude + 1, currY, currX - 1])
                seenPositions.add((currY, currX - 1))
    return totalPeaks

def countTrails(map: list[list[int]], trailHeads: list[tuple[int, int, int]]) -> int:
    totalTrails = 0
    height, width = len(map), len(map[0])
    for head in trailHeads:
        queue = deque([(0, [head])])
        while queue:
            altitude, currentTrail = queue.popleft()
            currY, currX = currentTrail[-1]
            if altitude == 9:
                totalTrails += 1
                continue
            if currY > 0 and map[currY - 1][currX] == altitude + 1: # UP
                queue.append((altitude + 1, currentTrail + [(currY - 1, currX)]))
            if currX < width - 1 and map[currY][currX + 1] == altitude + 1: # RIGHT
                queue.append((altitude + 1, currentTrail + [(currY, currX + 1)]))
            if currY < height - 1 and map[currY + 1][currX] == altitude + 1: # DOWN
                queue.append((altitude + 1, currentTrail + [(currY + 1, currX)]))
            if currX > 0 and map[currY][currX - 1] == altitude + 1: #LEFT
                queue.append((altitude + 1, currentTrail + [(currY, currX - 1)]))
    return totalTrails

if __name__ == "__main__":
    map, trailHeads = processInput()
    print(f'Part one: {graphify(map, trailHeads)}')
    print(f'Part two: {countTrails(map, trailHeads)}')
