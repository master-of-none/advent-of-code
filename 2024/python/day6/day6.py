from collections import defaultdict

def read_file():
    with open("input.txt", "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    
    return grid

def puzzle_1(grid):
    directions = {"^":(0,-1), ">":(1,0), "<": (-1,0), "v":(0,1)}
    right_turn = {"^":">", ">":"v", "v":"<", "<":"^"}
    
    ROWS = len(grid)
    COLS = len(grid[0])
    
    for y in range(ROWS):
        for x in range(COLS):
            if grid[y][x] in directions:
                guard_pos = (x,y)
                guard_dir = grid[y][x]
                break
    
    visited = set()
    visited.add(guard_pos)
    
    while True:
        x, y = guard_pos
        dx, dy = directions[guard_dir]
        next_pos = (x + dx, y + dy)
        
        if 0 <= next_pos[0] < COLS and 0 <= next_pos[1] < ROWS:
            if grid[next_pos[1]][next_pos[0]] == "#":
                guard_dir = right_turn[guard_dir]
            else:
                guard_pos = next_pos
                visited.add(guard_pos)
        else:
            break
    
    return len(visited)

def puzzle_2(grid):
    directions = {"^":(0,-1), ">":(1,0), "<": (-1,0), "v":(0,1)}
    right_turn = {"^":">", ">":"v", "v":"<", "<":"^"} 
    
    def simulate_patrol(grid, start_pos, start_dir):
        visited = set()
        path = []
        guard_pos, guard_dir = start_pos, start_dir
        
        while True:
            state = (guard_pos, guard_dir)
            
            if state in visited:
                return True
            
            visited.add(state)
            path.append(state)
            
            x, y = guard_pos
            dx, dy = directions[guard_dir]
            next_pos = (x + dx, y + dy)
            
            if 0 <= next_pos[0] < len(grid[0]) and 0 <= next_pos[1] < len(grid):
                if grid[next_pos[1]][next_pos[0]] == "#":
                    guard_dir = right_turn[guard_dir]
                else:
                    guard_pos = next_pos
            else:
                return False
    
    ROWS, COLS = len(grid), len(grid[0])
    for y in range(ROWS):
        for x in range(COLS):
            if grid[y][x] in directions:
                start_pos = (x, y)
                start_dir = grid[y][x]
                break
    
    res = 0
    for y in range(ROWS):
        for x in range(COLS):
            if grid[y][x] == "." and (x, y) != start_pos:
                grid[y][x] = "#"
                
                if simulate_patrol(grid, start_pos, start_dir):
                    res += 1
                
                grid[y][x] = "."
    
    return res
    
    
    

if __name__ == "__main__":
    grid = read_file()
    res1 = puzzle_1(grid)
    print(f"The Puzzle 1 Solution is: {res1}")
    
    res2 = puzzle_2(grid)
    print(f"The Puzzle 2 Solution is {res2}")