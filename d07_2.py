import re

def read_puzzle(file):
    puzzle = []
    for line in open(file).read().splitlines():
        l = list(map(int, re.findall("-?\\d+", line)))
        puzzle.append([l[0], l[1:]])
    return puzzle  

def equation_is_valid(v, eq, task1):
    if (eq[0] > v) : return False
    if len(eq) == 1: return v == eq[0]
    if equation_is_valid(v, [eq[0] + eq[1]] + eq[2:], task1): return True
    if equation_is_valid(v, [eq[0] * eq[1]] + eq[2:], task1): return True
    if not task1 and equation_is_valid(v, [int(str(eq[0])+str(eq[1]))] + eq[2:], task1): return True
    return False

def solve(puzzle, task1):
    solution = 0
    for v, eq in puzzle:
        solution += equation_is_valid(v, eq, task1) * v
    return solution

puzzle = read_puzzle('d07.txt')
print("Task 1", solve(puzzle, True))
print("Task 2", solve(puzzle, False))