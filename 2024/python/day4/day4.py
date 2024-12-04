def read_file():
    with open("input.txt", "r") as file:
        grid = [line.strip() for line in file.readlines()]
    
    return grid

def puzzle_1(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    res = 0
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                for dx,dy in directions:
                    found = True
                    
                    for k in range(word_len):
                        nx, ny = i + k * dx, j + k * dy
                        
                        if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
                            found = False
                    
                    if found:
                        res += 1
    
    return res

def puzzle_2(grid):
    rows = len(grid)
    cols = len(grid[0])
    res = 0
    
    def check_mas(x, y, dx, dy):
        mas = "MAS"
        sam = "SAM"
        chars = []
        
        for i in range(3):
            nx, ny = x + i * dx, y + i * dy
            
            if 0 <= nx < rows and 0 <= ny < cols:
                chars.append(grid[nx][ny])
            
            else:
                return False

        return "".join(chars) == mas or "".join(chars) == sam
    
    for i in range(rows):
        for j in range(cols):
            if (check_mas (i, j, 1, 1) and check_mas(i+2, j, -1, 1)):
                res += 1
    
    return res

if __name__ == "__main__":
    
    word = "XMAS"
    grid = read_file()
    res1 = puzzle_1(grid, word)
    print(f"The Puzzle 1 Solution is: {res1}")

    res2 = puzzle_2(grid)
    print(f"The Puzzle 1 Solution is: {res2}")
    