def read_file():
    with open("input.txt", "r") as filename:
        input = filename.readline()
    
    return input

def puzzle_1(input):
    x, y  = 0, 0
    visited = set()
    visited.add((x,y))
    
    directions = {'^':(0,1), "v":(0, -1), "<":(-1,0), ">":(1,0)}
    
    for d in input:
        dx, dy = directions[d]
        x += dx
        y += dy
        
        visited.add((x,y))
    
    return len(visited)

def puzzle_2(input):
    x_santa, y_santa = 0,0
    x_robo, y_robo = 0,0
    visited = set()
    visited.add((x_santa, y_santa))
    directions = {'^':(0,1), "v":(0, -1), "<":(-1,0), ">":(1,0)}

    for i, d in enumerate (input):
        dx, dy = directions[d]
        
        if i % 2 == 0:
            x_santa += dx
            y_santa += dy
            visited.add((x_santa, y_santa))
        else:
            x_robo += dx
            y_robo += dy
            visited.add((x_robo, y_robo))
    
    return len(visited)

    
if __name__ == "__main__":
    input = read_file()
    res1 = puzzle_1(input)
    print(f'The Puzzle 1 Solution is: {res1}')
    res2 = puzzle_2(input)
    print(f'The Puzzle 2 Solution is: {res2}')
