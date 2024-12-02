f = open("input.txt", "r")
lines = f.readlines()
left, right = [], []

for l in lines:
    left_side, right_side = map(int, l.split())
    left.append(left_side)
    right.append(right_side)

left.sort()
right.sort()
res1 = 0

for x, y in zip(left, right):
    dist = abs(x - y)
    # print(dist)
    res1 += dist

print(f'The Puzzle 1 Solution is: {res1}')

# Part 2

# left = [3,4,2,1,3,3]
# right = [4,3,5,3,9,3]
hashmap_right = {}
for n in right:
    hashmap_right[n] = 1 + hashmap_right.get(n, 0)

res2 = 0
for n in left:
    res2 += n * hashmap_right.get(n, 0)

print(f'The Puzzle 2 Solution is: {res2}')