from collections import defaultdict
import itertools

def read_puzzle(file):
    coords = set()
    freqs = defaultdict(set)
    for y, line in enumerate (open(file).read().splitlines()):
        for x, c in enumerate(line):
            coords.add((x,y))
            if c != ".": freqs[c].add((x,y))   
    return [coords, freqs]

def add_point(p1,p2):
    return (p1[0]+p2[0], p1[1]+p2[1])

def neg_point(p1):
    return (-p1[0], -p1[1])

def sub_point(p1,p2):
    return add_point(p1, neg_point(p2))

def find_antinodes(coords, coords_for_f, antinodes:set, task1):
    for p1, p2 in itertools.combinations(coords_for_f, 2):
        delta = sub_point(p1, p2)
        points = set()
        if task1: 
            points.add(add_point(p1, delta))
            points.add(sub_point(p2, delta))
            points = points.intersection(coords)
        else:
            for delta in [delta, neg_point(delta)]:
                next = p1
                while( next in coords):
                    points.add(next)
                    next = add_point(next, delta) 
        antinodes = antinodes.union(points)
    return antinodes

def solve(puzzle, task1):
    coords, freqs = puzzle
    antinodes = set()
    for f in freqs:
        antinodes = find_antinodes(coords, freqs[f], antinodes, task1)
    return len(antinodes)

puzzle = read_puzzle('d08.txt')
print("Task 1", solve(puzzle, True))
print("Task 2", solve(puzzle, False))