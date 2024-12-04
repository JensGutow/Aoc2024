import re
def read_puzzle(file):
    text = open(file).read()
    return re.findall("mul\\(\\d+,\\d+\\)|don't\\(\\)|do\\(\\)", text)

def solve(puzzle, part1):
    value = 0
    do_ = True
    for p in puzzle:
        if p == "do()": do_ = True
        elif p == "don't()": do_ = False
        elif not part1 and not do_: continue
        else:
            a, b = list(map(int, re.findall("\\d+",p)))
            value += a*b
    return value
    
puzzle = read_puzzle('d03.txt')
print("Task 1", solve(puzzle, True))
print("Task 2", solve(puzzle, False))