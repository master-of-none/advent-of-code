def apply_instruction(grid, line):
    words = line.split()
    if words[0] == "turn":
        action = words[1]
        start = list(map(int, words[2].split(',')))
        end = list(map(int, words[4].split(',')))
    
    elif words[0] == "toggle":
        action = "toggle"
        start = list(map(int, words[1].split(',')))
        end = list(map(int, words[3].split(',')))

    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            if action == "on":
                grid[x][y] = 1
            elif action == "off":
                grid[x][y] = 0
            elif action == "toggle":
                grid[x][y] = 1 - grid[x][y]

def parse_file(grid):
    with open("input.txt", "r") as f:
        for line in f:
            apply_instruction(grid, line.strip())
    
    return grid

def puzzle_1(grid):
    res = sum(sum(row) for row in grid)
    return res

def puzzle_2(grid):
    
    def apply_instruction_part_2(grid, line):
        words = line.split()
        if words[0] == "turn":
            action = words[1]
            start = list(map(int, words[2].split(',')))
            end = list(map(int, words[4].split(',')))
        elif words[0] == "toggle":
            action = "toggle"
            start = list(map(int, words[1].split(',')))
            end = list(map(int, words[3].split(',')))
        
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                if action == "on":
                    grid[x][y] += 1
                elif action == "off":
                    grid[x][y] = max(0, grid[x][y] - 1)
                elif action == "toggle":
                    grid[x][y] += 2
        
        return grid
    
    with open("input.txt", "r") as f:
        for line in f:
            apply_instruction_part_2(grid, line.strip())
    
    res = sum(sum(row) for row in grid)
    return res

if __name__ == "__main__":
    GRID_SIZE = 1000
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    grid = parse_file(grid)
    res1 = puzzle_1(grid)
    print(f"The Puzzle 1 Solutions is: {res1}")
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    res2 = puzzle_2(grid)
    print(f"The Puzzle 1 Solutions is: {res2}")