# https://adventofcode.com/2024/day/3
import re, operator

def main():
    memoryDump = open("day03.txt").read()
    multParampattern = r"mul\((\d{0,3}),(\d{0,3})\)"
    cutFatPattern = r"don't\(\)(?:.|\n)*?do\(\)"
    sumProducts = lambda text : sum([operator.mul(*map(int, group)) for group in re.findall(multParampattern, text)])
    print(f"Part one answer: {sumProducts(memoryDump)}")
    print(f"Part two answer: {sumProducts(re.sub(cutFatPattern, '', memoryDump))}")

main()