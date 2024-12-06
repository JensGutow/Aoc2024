DIRECTION = [[0,-1], [1,0], [0,1],[-1,0]]
                                   
def read_puzzle(file):
    d = dict()
    start_pos = None
    text = open(file).read().splitlines()
    free_positions = set()
    for y, line in enumerate(text):
        for x, c in enumerate(line):
            d[(x,y)] = c
            if c == ".": free_positions.add((x,y))
            elif c == "^" : 
                start_pos = (x,y)
                d[(x,y)] = "."
    return free_positions, start_pos, d

def addDir(l1, l2):
    return (l1[0]+l2[0], l1[1]+l2[1])

def findPath(pos:list, d:dict):
    dir = 0
    locations = {pos}
    loop_detector = {(pos, dir)}
    loop_detected = False
    while(True):
        pos_next = addDir(pos, DIRECTION[dir])
        if pos_next not in d.keys(): break
        if d[pos_next] == "#": 
            dir = (dir + 1)%(len(DIRECTION))
            continue
        pos = pos_next
        locations.add(pos)
        if (loop_detected := (pos, dir) in loop_detector):
            break
        loop_detector.add((pos,dir))
    return loop_detected, len(locations)
    
def solve(free_positions:set, pos:list, d:dict):
    _, part1 = findPath(pos, d)
    part2 = 0
    print(f"Number of free positions: {len(free_positions)}")
    for i, free_pos in enumerate(free_positions):
        d[free_pos] = "#"
        if(i%1000 == 0): print(f"step:{i}")
        part2 += findPath(pos, d)[0]
        d[free_pos] = "."
    return part1, part2

puzzle = read_puzzle('d06.txt')
print("Task 1/2", solve(*puzzle))