def read_file(input):
    with open("input.txt", "r") as file:
        for line in file:
            dimensions = list(map(int, line.strip().split('x')))
            input.append(dimensions)
    
    return input

def puzzle_1(input):
    res = 0
    for i in range(len(input)):
        l,w,h = input[i][0], input[i][1], input[i][2]
        
        surface_area = 2 * l * w + 2 * w * h + 2 * h * l
        input[i].sort()
        slack = input[i][0] * input[i][1]
        
        res += surface_area + slack
    
    return res

def puzzle_2(input):
    res = 0
    for i in range(len(input)):
        l,w,h = input[i][0], input[i][1], input[i][2]
        bow_length = l * w * h
        input[i].sort()
        perimeter = 2 * (input[i][0] + input[i][1])
        res += bow_length + perimeter
    
    return res
    
if __name__ == "__main__":
    input = []
    input = read_file(input)
    input_copy = input.copy()
    res1 = puzzle_1(input)
    
    res2 = puzzle_2(input_copy)
    print(res1)
    print(res2)