with open("input.txt", "r") as f:
    input = f.read()

res = 0
pos = 0
for i in range(len(input)):
    if input[i] == '(':
        res += 1
    
    elif input[i] == ')':
        res -= 1

    if res < 0 and pos == 0:
        pos = i + 1
print(res)
print(pos)