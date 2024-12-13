from collections import defaultdict
from math import log10
from multiprocessing import Pool, cpu_count
from functools import partial
from time import time
startTime = time()

def blinkNStones(input, blinks = 25):
    generation : defaultdict = defaultdict(int)
    for stone in input: # initial generation -- family tree = 1 individual
        generation[stone] = 1
    for _ in range(blinks):
        children : defaultdict = defaultdict(int)
        for stone, ancestorCount in generation.items(): # grow next generation
            if stone == 0:
                children[1] += ancestorCount
            elif (int(log10(stone)) + 1) & 1: # odd length of digits
                children[stone * 2024] += ancestorCount
            else: # even length of digits
                strStone = str(stone)
                children[int(strStone[int(len(strStone)/2):])] += ancestorCount
                children[int(strStone[:int(len(strStone)/2)])] += ancestorCount
        generation = children # pass torch to next generation
    return sum(generation.values())


def blinkN(input, blinks = 25): # slower
    with Pool(cpu_count() - 1) as pool:
        return sum(pool.map(partial(blinkNStones, blinks=blinks), [[stone] for stone in input]))

def processInput():
    with open("day11.txt") as file:
        return [int(word) for word in file.readline().split()]
    
if __name__ == "__main__":
    input = processInput()
    print(f'Part one: {blinkNStones(input)}')
    print(f'Time to finish {time() - startTime}')
    startTime = time()
    print(f'Part two: {blinkNStones(input, 75)}')
    print(f'Time to finish {time() - startTime}')