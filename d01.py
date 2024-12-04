def read_puzzle(file):
    puzzle = []
    for line in open(file).read().splitlines():
        line = line.split("   ")
        puzzle.append([int(line[0]), int(line[1])])
    return puzzle

def solve(puzzle):
    p = [list(p) for p in zip(*puzzle)]
    
    part2 = 0
    s0 = set(p[0]).intersection(set(p[1]))
    for s in s0:
        n = p[0].count(s) * s * p[1].count(s)
        part2 += n

    part1 = 0
    p[0].sort()
    p[1].sort()
    part1 = sum([abs(a-b) for a,b in zip(*p)])

    return part1, part2
    
puzzle = read_puzzle('d01.txt')

print("Task 1/2", solve(puzzle))