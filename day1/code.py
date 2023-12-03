import sys
file = open(sys.argv[1]).read().strip()
result = 0

for line in file.split('\n'):
    digits = []
    for c in line:
        if c.isdigit():
            digits.append(c)
    temp = int(digits[0]+digits[-1])
    result += temp
print(result)
    