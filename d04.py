import re
def read_puzzle(file):
    puzzle = []
    for line in open(file).read().splitlines():
        l = re.findall(".", line)
        puzzle.append(l)
    return puzzle



def getDiags1(puzzle):
    y_max = len(puzzle)
    x_max = len(puzzle[0])
    assert(y_max == x_max)
    diags = []

    for l in range(y_max):
        diag = []
        diag2 = []
        for x in range(l+1):
            x_cord = x
            y_cord = l-x
            diag.append(puzzle[y_cord][x_cord])            
            x_cord = x_max-l+x-1
            y_cord = x
            diag2.append(puzzle[y_cord][x_cord])
        diags.append(diag)
        diags.append(diag2)
        
    for l in range(y_max-1):
        diag = []
        diag2 = []
        for x in range(0,l+1):
            x_cord = y_max - 1 - x
            y_cord = y_max - l + x-1
            diag.append(puzzle[y_cord][x_cord])
            x_cord = x
            y_cord = y_max - l + x-1
            diag2.append(puzzle[y_cord][x_cord])
        diags.append(diag)
        diags.append(diag2)
    return diags

def getLines(puzzle):
    lines = []
    for l in puzzle:
        lines.append(l)
    diags = getDiags1(puzzle)
    for diag in diags:
        lines.append(diag)
    transp = list(zip(*puzzle))
    for l in transp:
        lines.append(l)
    return lines

def solve(puzzle):
    part1 = 0
    lines = getLines(puzzle)
    for line in lines:
        part1 += len(re.findall("XMAS", "".join(line)))
        part1 += len(re.findall("SAMX", "".join(line)))
    return part1

def solvePart2(puzzle):
    l = len(puzzle)
    part2 = 0
    for x in range(1,l-1):
        for y in range(1,l-1):
            if puzzle[y][x] != "A" : continue
            if set([puzzle[y-1][x-1], puzzle[y+1][x+1]])!=set(["M", "S"]):continue
            if set([puzzle[y-1][x+1], puzzle[y+1][x-1]])!=set(["M", "S"]):continue
            part2 += 1
    return part2

puzzle = read_puzzle('d04.txt')
print("Task 1", solve(puzzle))
print("Task 2", solvePart2(puzzle))