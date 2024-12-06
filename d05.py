import re
import copy

def readNumbers(s):
    l = re.findall("\\d+", s)
    return list(map(int,l))

def read_puzzle(file):
    puzzle = []
    text = open(file).read().split("\n\n")
    rules = {tuple(readNumbers(rule))  for rule in text[0].split("\n")}
    updates = [readNumbers(update) for update  in text[1].split("\n")]
    return (rules, updates)

def checkRules(rules, left, other):
    s1 = {(o, left) for o in other}
    return not s1.intersection(rules)

def solve(puzzle):
    part1 = part2 = 0
    rules, updates = puzzle
    for update in updates:
        isValid = True
        for i, left in enumerate(update):
            if not checkRules(rules, left, update[i+1:]):
                isValid = False
                break
        if isValid:
            part1 += update[(len(update))//2]
        else:
            correction = []
            while update:
                for i in range(len(update)):
                    u = update.pop(i)
                    if checkRules(rules,u, update):
                        correction.append(u)
                        break
                    else:
                        update = update[:i] + [u] + update[i:]
            part2 += correction[len(correction)//2]
    return part1, part2
    
puzzle = read_puzzle('d05.txt')
print("Task 1/2", solve(puzzle))