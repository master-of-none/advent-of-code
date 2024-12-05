from collections import defaultdict, deque

def read_file():
    with open("input.txt", "r") as filename:
        content = filename.read()
    
    rules_raw, updates_raw = content.strip().split("\n\n")
    return rules_raw, updates_raw

def parse_rules(rules_raw):
    ordering_rules = []
    for line in rules_raw.strip().split("\n"):
        x, y = map(int, line.split("|"))
        ordering_rules.append((x, y))
    return ordering_rules

def parse_updates(updates_raw):
    return [list(map(int, update.split(","))) for update in updates_raw.strip().split("\n")]

def is_valid_update(update, rules):
    index_map = {page: idx for idx, page in enumerate(update)}
        
    for x, y in rules:
        if x in update and y in update:
            if index_map[x] > index_map[y]:
                return False
    return True

def reorder_update(update, rules):
    # Build the graph
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages = set(update)
    
    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1
            in_degree.setdefault(x, 0)
    
    # Topological sorting using Kahn's Algorithm
    queue = deque([page for page in pages if in_degree[page] == 0])
    sorted_update = []
    
    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_update

def puzzle_1(rules_raw, updates_raw):
    ordering_rules = parse_rules(rules_raw)
    updates = parse_updates(updates_raw)
    
    res = 0
    for update in updates:
        if is_valid_update(update, ordering_rules):
            middle_page = update[len(update) // 2]
            res += middle_page

    return res

def puzzle_2(rules_raw, updates_raw):
    ordering_rules = parse_rules(rules_raw)
    updates = parse_updates(updates_raw)
    
    res = 0
    for update in updates:
        if not is_valid_update(update, ordering_rules):
            reordered_update = reorder_update(update, ordering_rules)
            middle_page = reordered_update[len(reordered_update) // 2]
            res += middle_page
    
    return res

if __name__ == "__main__":
    rules_raw, updates_raw = read_file() 
    res1 = puzzle_1(rules_raw, updates_raw)
    print(f"The Puzzle 1 Solution is: {res1}")
    
    res2 = puzzle_2(rules_raw, updates_raw)
    print(f"The Puzzle 2 Solution is: {res2}")