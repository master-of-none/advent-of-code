import re

# input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
def read_file():
    input = ""
    with open("input.txt", "r") as file:
        for line in file:
            input += line

    return input

def puzzle_1(input):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    input_list = re.findall(pattern, input)
    # print(input_list)

    res = 0
    for val in input_list:
        numbers = val[4:-1].split(",")
        x, y = int(numbers[0]), int(numbers[1])
    
    res += (x * y)

    print(f"The Puzzle 1 solution is {res}")

def puzzle_2(input):
    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)" 
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    input_list = re.findall(f"{mul_pattern}|{do_pattern}|{dont_pattern}", input)
    
    flag = True
    res = 0
    for val in input_list:
        if val == "do()":
            flag = True
        elif val == "don't()":
            flag = False
        elif val.startswith("mul(") and flag:
            numbers = val[4:-1].split(",")
            x, y = int(numbers[0]), int(numbers[1])
            res += (x * y)
    
    print(f"The Puzzle 2 solution is: {res}")


if __name__ == "__main__":
    input = read_file()
    puzzle_1(input=input)
    puzzle_2(input=input)
    