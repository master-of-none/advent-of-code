with open("input.txt", "r") as input_file:
    map = [list(map(int, row.strip())) for row in input_file.readlines()]
    size = len(map)

trailheads = [(x, y) for x in range(size) for y in range(size) if map[x][y] == 0]

def get_next_pos(x, y):
    next_pos = []
    for dx, dy in {(0, 1), (0, -1), (1, 0), (-1, 0)}:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < size and 0 <= new_y < size and map[new_x][new_y] == map[x][y] + 1:
            next_pos.append((new_x, new_y))
    return next_pos


def trailhead_score_rec(pos: tuple, cached_9_pos: set, root: bool = False):
    if map[pos[0]][pos[1]] == 9:
        cached_9_pos.add(pos)
    for next_pos in get_next_pos(*pos):
        trailhead_score_rec(next_pos, cached_9_pos)
    if root:
        return len(cached_9_pos)


sum_score = sum([trailhead_score_rec(trailhead, set(), root=True) for trailhead in trailheads])

print(f"Sum of the scores of all trailheads: {sum_score}")

def trailhead_distinct_score_rec(pos: tuple):
    if map[pos[0]][pos[1]] == 9:
        return 1
    return sum([trailhead_distinct_score_rec(next_pos) for next_pos in get_next_pos(*pos)])


sum_rating = sum([trailhead_distinct_score_rec(trailhead) for trailhead in trailheads])

print(f"Sum of the ratings of all trailheads: {sum_rating}")