from collections import Counter

def read_file(filename):
    with open(filename, 'r') as file:
        stones = list(map(int, file.readline().strip().split()))

    return stones

def puzzle_1(stones, blinks):
    for i in range(blinks):
        print(f'Running Part 1 Loop: {i}')
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                new_stones.extend([left,right])
            else:
                new_stones.append(stone * 2024)
        
        stones = new_stones
    
    return len(stones)

def puzzle_2(stones, blinks):
    stones_count = Counter(stones)
    
    for i in range(blinks):
        print(f"Running Part 2 Loop: {i}")
        new_counts = Counter()
        for stone, count in stones_count.items():
            if stone == 0:
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                new_counts[left] += count
                new_counts[right] += count
            else:
                new_counts[stone * 2024] += count
        
        stones_count = new_counts
    
    return sum(stones_count.values())

if __name__ =="__main__":
    stones = read_file("input.txt")
    res1 = puzzle_1(stones, 25)

    
    stones = read_file("input.txt")
    res2 = puzzle_2(stones, 75)
    
    print(f"The Puzzle 1 Solution is: {res1}")
    print(f"The Puzzle 2 Solution is: {res2}")
    