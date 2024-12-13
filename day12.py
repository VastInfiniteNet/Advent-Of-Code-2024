from collections import defaultdict, deque
import time
from functools import cmp_to_key

def processInput():
    plantIDs = defaultdict(str)
    regions = defaultdict(list)
    with open("day12.txt") as file:
        y = 0
        for line in file:
            x = 0
            for plant in line.strip():
                plantIDs[(y,x)] = plant
                regions[plant].append((y,x))
                x += 1
            y += 1
    return (plantIDs, regions)

DIR = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
DIR_DIR, DIR_VECS = list(DIR.keys()), list(DIR.values())
def calcRegionPricing(plantIDs: defaultdict, region: str, regionPlants : set[tuple[int, int]]):
    price = 0
    visitedPlants = set()
    neighbor = lambda point, dirVec: (point[0] + dirVec[0], point[1] + dirVec[1])

    for plant in regionPlants:
        if plant in visitedPlants:
            continue
        blobPerimeter = 0
        blobArea = 0
        queue = deque([plant])
        while queue:
            current = queue.popleft()
            visitedPlants.add(current)
            blobArea += 1
            for dir in DIR_VECS:
                nextDoor = neighbor(current, dir)
                if plantIDs[nextDoor] != region:
                    blobPerimeter += 1
                elif nextDoor not in visitedPlants and nextDoor not in queue:
                    queue.append(nextDoor)
        price += blobArea * blobPerimeter

    return price

def compareEdges(dir):
    def cmpFunc(edge1, edge2):
        if dir in ["N", "S"]:
            return edge1[0] - edge2[0]
        return edge1[1] - edge2[1]
    return cmpFunc

def countSides(edges):
    sideCount = 0
    for dir in edges:
        dirEdges = edges[dir]
        dirVec = DIR[dir]
        dimBreak, dimSkip = (abs(dirVec[1]), abs(dirVec[0])) 
        dirSideCount = 1
        dirEdges.sort(key=cmp_to_key(compareEdges(dir)))
        for i in range(1, len(dirEdges)):
            prev, curr = dirEdges[i - 1], dirEdges[i]
            if prev[dimBreak] != curr[dimBreak]: # check if edges are separated by invalid dimensions
                dirSideCount += 1
            elif abs(prev[dimSkip] - curr[dimSkip]) > 1: # check if gap between edges
                dirSideCount += 1
        sideCount += dirSideCount
        #print(f'{dir}, {dimBreak, dimSkip}, {dirSideCount}: {dirEdges}')
    #print(f'Counted {sideCount} sides')
    return sideCount

def calcRegionPricingSides(plantIDs: defaultdict, region: str, regionPlants : set[tuple[int, int]]):
    price = 0
    visitedPlants = set()
    neighbor = lambda point, dirVec: (point[0] + dirVec[0], point[1] + dirVec[1])
    #print(f'\nRegion {region}')
    for plant in regionPlants:
        if plant in visitedPlants:
            continue
        blobPerimeter = defaultdict(list)
        blobArea = 0
        queue = deque([plant])
        while queue:
            current = queue.popleft()
            visitedPlants.add(current)
            blobArea += 1
            for dir in DIR:
                nextDoor = neighbor(current, DIR[dir])
                if plantIDs[nextDoor] != region:
                    blobPerimeter[dir].append(nextDoor)
                elif nextDoor not in visitedPlants and nextDoor not in queue:
                    queue.append(nextDoor)
        #print(f'Area of {blobArea}')
        price += blobArea * countSides(blobPerimeter)
    print(f"\n\n\nPrice of '{region}': {price}\n\n\n")
    return price

plantIDs, regions = processInput()
calc = lambda func: sum([func(plantIDs, region, regions[region]) for region in regions])
print(f'Part one: {calc(calcRegionPricing)}')
print(f'Part two: {calc(calcRegionPricingSides)}')