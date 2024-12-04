import re
def read_puzzle(file):
    puzzle = []
    for line in open(file).read().splitlines():
        l = re.findall("-?\\d+", line)
        puzzle.append(list(map(int,l)))
    return puzzle

def checkLine(line):
    A = all([(0 < (a-b) <= 3) for a,b in zip(line[0:-1], line[1:])])
    B = all([(0 < (b-a) <= 3) for a,b in zip(line[0:-1], line[1:])])
    return A or B

def solve(puzzle):
    part1 = deltaPart2 = 0
    for line in puzzle:
        check = checkLine(line)
        part1 += check
        if not check:
            l = len(line)
            for i in range(l):
                if checkLine(line[0:i] + line[i+1:l]):
                    deltaPart2 += 1
                    break
    return part1, part1 + deltaPart2
    
puzzle = read_puzzle('d02.txt')
print("Task 1/2", solve(puzzle))