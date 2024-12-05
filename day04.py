# https://adventofcode.com/2024/day/4

WORD_SIZE = 4
crossWord = [[char for char in line.strip()] for line in open("day04.txt")]
height, width = len(crossWord), len(crossWord[0])

def part1():
    total = 0
    TARGET_WORDS = [[char for char in "XMAS"], [char for char in "SAMX"]]
    for y in range(height):
        for x in range(width): # only need to check 4/8 directions
            if crossWord[y][x] not in "SX": 
                continue
            if x <= width - WORD_SIZE and crossWord[y][x:x+WORD_SIZE] in TARGET_WORDS: #horizontal right check
                total += 1
            if y <= height - WORD_SIZE and [crossWord[y+a][x] for a in range(WORD_SIZE)] in TARGET_WORDS: #vertical down check
                total += 1
            if y <= height - WORD_SIZE and x <= width - WORD_SIZE and [crossWord[y+a][x+a] for a in range(WORD_SIZE)] in TARGET_WORDS: #down right diagonal check
                total += 1
            if y <= height - WORD_SIZE  and x + 1 >= WORD_SIZE  and [crossWord[y+a][x-a] for a in range(WORD_SIZE)] in TARGET_WORDS: #down left diagonal check
                total += 1
    return total

def part2():
    total = 0
    targets = ["MS", "SM"]
    for y in range(1, height - 1):  # ignore border positions, they are can't form full X-MAS 
        for x in range(1, width - 1): 
            if crossWord[y][x] != 'A': # only A can be center of X-MAS
                continue
            if crossWord[y-1][x-1] + crossWord[y+1][x+1] in targets and crossWord[y-1][x+1] + crossWord[y+1][x-1] in targets:
                total += 1
    return total

print(f"Day one: {part1()}")
print(f"Day one: {part2()}")