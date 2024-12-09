from collections import defaultdict
from itertools import combinations

def f(grid):
    n = len(grid)
    def find_antinodes(p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        nx, ny = x1 - (x2 - x1), y1 - (y2 - y1)
        mx, my = x2 + (x2 - x1), y2 + (y2 - y1)


        if 0 <= nx < n and 0 <= ny < n:
            yield (nx, ny)
        if 0 <= mx < n and 0 <= my < n:
            yield (mx, my)

    groups = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if grid[i][j] != ".":
                groups[grid[i][j]].append((i, j))

    antinodes = set()

    for freq, arr in groups.items():
        for a, b in combinations(arr, r=2):
            for node in find_antinodes(a, b):
                antinodes.add(node)
    return len(antinodes)



def f2(grid):
    n = len(grid)
    def find_antinodes2(p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        # slope
        delta_x, delta_y = x2 - x1, y2 - y1
        i = 0
        while 1:
            nx, ny = x2 - delta_x * i, y2 - delta_y * i
            if 0 <= nx < n and 0 <= ny < n:
                i += 1
                yield (nx, ny)
            else:
                break
        i = 0
        while 1:
            nx, ny = x2 + delta_x * i, y2 + delta_y * i
            if 0 <= nx < n and 0 <= ny < n:
                i += 1
                yield (nx, ny)
            else:
                break

    groups = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if grid[i][j] != ".":
                groups[grid[i][j]].append((i, j))

    antinodes = set()

    for freq, arr in groups.items():
        for a, b in combinations(arr, r=2):
            for node in find_antinodes2(a, b):
                antinodes.add(node)
    return len(antinodes)


with open('input.txt') as file:
    data = file.read().strip()


lines = data.split('\n')
grid = []
for line in lines:
    grid.append(list(line))

print(f(grid))
print(f2(grid))