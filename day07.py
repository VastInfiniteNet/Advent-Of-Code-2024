from time import time
import multiprocessing 
from functools import partial
import line_profiler
startTime = time()

equations = []
solved = []

@line_profiler.profile
def solvable(ops, eq):
    goal, numbers = eq
    if (goal, numbers) in solved:
        return goal
    numCount = len(numbers)

    for seed in range(ops**numCount):
        candidateTotal = numbers[0]
        for i in range(1,numCount):
            opCode = seed % ops
            num = numbers[i]
            match opCode:
                case 0 :
                    candidateTotal += num
                case 1 : 
                    candidateTotal *= num
                case 2 :
                    match num:
                        case num if num < 10:
                            candidateTotal = candidateTotal * 10 + num
                        case num if num < 100:
                            candidateTotal = candidateTotal * 100 + num
                        case _ :
                            candidateTotal = candidateTotal * 1000 + num
            if candidateTotal > goal: # seed missed goal, try another seed
                break
            seed = (seed - opCode) / ops
        if  candidateTotal == goal: # seed successfully generated goal
            solved.append((goal, numbers))
            return goal
    return 0 # no valid seed

def processInput():
    with open("day07.txt") as file:
        for line in file:
            lineBroken = line.split(": ")
            equations.append((int(lineBroken[0]), [int(num) for num in lineBroken[1].split()]))

def solve(opCount):
    with multiprocessing.Pool() as pool:
        return sum(pool.map(partial(solvable, opCount), equations))

if __name__ == '__main__':
    processInput()
    print(f'Part one: {solve(2)}')
    print(f'Finished in {time() - startTime}')
    print(f'Part two: {solve(3)}')
    print(f'Finished in {time() - startTime}')