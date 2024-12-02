# https://adventofcode.com/2024/day/2

def validateReport(report, allowedMistakes = False):
    startDirection = -1 if report[1] - report[0] < 0 else 1
    for i in range(len(report) - 1):
        levelDiff = report[i+1] - report[i]
        currDirection = -1 if levelDiff < 0 else 1
        if (
            startDirection != currDirection or
            abs(levelDiff) > 3 or 
            abs(levelDiff) == 0
        ):
            if allowedMistakes: # some error in a 3 wide problem window X Y Y Y X
                                # try to remove a level and retest
                return  (   validateReport(report[0:i-1] + report[i:], False) or    # remove left side of window
                            validateReport(report[0:i] + report[i+1:], False) or    # remove center of window
                            validateReport(report[0:i+1] + report[i+2:], False))    # remove right side of window
            else:
                return False
    return True

def countReports(reports, allowedMistake):
    safeCount = 0
    for report in reports:
        if validateReport(report, allowedMistake):
                safeCount += 1
    return safeCount

def processInput():
    reports = []
    with open("day02.txt") as file:
        for line in file:
            reports.append(list(map(int, line.strip().split())))
    return reports

def main():
    reports = processInput()

    print(f"Part one answer: {countReports(reports, False)}")
    print(f"Part two answer: {countReports(reports, True)}")

main()