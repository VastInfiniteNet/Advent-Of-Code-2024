# https://adventofcode.com/2024/day/2

def validateReport(report, allowedMistakes):
    startDirection = -1 if report[1] - report[0] < 0 else 1
    for i in range(len(report) - 1):
        levelDiff = report[i+1] - report[i]
        currDirection = -1 if levelDiff < 0 else 1
        if startDirection != currDirection or abs(levelDiff) > 3 or abs(levelDiff) == 0:
            if not allowedMistakes:
                return False
            # some error in a 3 wide problem window X Y Y Y X, remove a level and retest
            return (validateReport(report[0:i-1] + report[i:], False) or    # remove left side of window
                    validateReport(report[0:i] + report[i+1:], False) or    # remove center of window
                    validateReport(report[0:i+1] + report[i+2:], False))    # remove right side of window
    return True

def processInput():
    with open("day02.txt") as file:
        return [list(map(int, line.strip().split())) for line in file]

def main():
    reports = processInput()
    countReports = lambda m: sum([validateReport(r, m) for r in reports])
    print(f"Part one answer: {countReports(False)}")
    print(f"Part two answer: {countReports(True)}")

main()