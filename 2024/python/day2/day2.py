input = []
with open("input.txt", "r") as file:
    for line in file:
        report = list(map(int,line.split()))
        input.append(report)

allowable = [1,2,3]
res = 0

def safe(report):
    direction = None
    for j in range(1, len(report)):
        diff = report[j] - report[j - 1]
        if abs(diff) not in allowable:
            return False
        if direction is None:
            direction = "increase" if diff > 0 else "decrease"
        elif (direction == "increase" and diff <= 0) or (direction == "decrease" and diff >= 0):
            return False
    return True

res1 = 0
for report in input:
    if safe(report):
        res1 += 1

res2 = 0
for report in input:
    if safe(report):
        res2 += 1
    else:
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if safe(modified_report):
                res2 += 1
                break

print(f'The Puzzle 1 solution is: {res1}')
print(f'The Puzzle 2 solution is: {res2}')