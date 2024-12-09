from itertools import product

def evaluate(numbers, operators):
    result = numbers[0]
    
    for i, operator in enumerate(operators):
        if operator == "+":
            result += numbers[i + 1]
        elif operator == "*":
            result *= numbers[i + 1]
        elif operator == "||":
            result = int(str(result) + str(numbers[i + 1]))
    
    return result

def can_produce_result(target, numbers, operator_set):
    num_operators = len(numbers) - 1
    operator_combo = product(operator_set, repeat=num_operators)
    
    for o in operator_combo:
        if evaluate(numbers, o) == target:
            return True
    
    return False

def puzzle_1(filename):
    res = 0
    with open(filename, "r") as file:
        for line in file:
            target, numbers = line.split(": ")
            target = int(target)
            numbers = list(map(int, numbers.split()))
            
            if can_produce_result(target, numbers, ['+', '*']):
                res += target
    
    return res

def puzzle_2(filename):
    res = 0
    with open(filename, "r") as file:
        for line in file:
            target, numbers = line.split(": ")
            target = int(target)
            numbers = list(map(int, numbers.split()))
            
            if can_produce_result(target, numbers, ["+", "*", "||"]):
                res += target
    
    return res

if __name__ == "__main__":
    res1 = puzzle_1("input.txt")
    print(f"The Puzzle 1 Solution is: {res1}")
    
    res2 = puzzle_2("input.txt")
    print(f"The Puzzle 1 Solution is: {res2}")