import re
import itertools
def read_puzzle(file):
    puzzle = []
    for line in open(file).read().splitlines():
        l = re.findall("-?\\d+", line)
        puzzle.append([l[0],l[1:]])
    return puzzle  

def eval_ausdruck(v1, op, v2):
    if op =="|": return int(v1+v2)
    else:  return eval(v1+op+v2)

def equation_is_valid(v,eq, task1):
    op_liste = "*+" if task1 else "|*+"
    ops = [op_liste for _ in range(len(eq)-1)]
    is_valid = False
    for op_list in itertools.product(*ops):
        value = int(eq[0])
        for i, op in enumerate(op_list, 1):
            value = eval_ausdruck(str(value), op, eq[i])
        if value > int(v): continue
        if (value == int(v)):
            is_valid = True
            break
    return is_valid

def solve(puzzle, task1):
    solution = 0
    for v, eq in puzzle:
        if equation_is_valid(v,eq, task1):
            solution += int(v)
    return solution

puzzle = read_puzzle('d07.txt')
print("Task 1", solve(puzzle, True))
print("Task 2", solve(puzzle, False))