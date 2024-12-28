def read_file():
    input = []
    with open("input.txt", "r") as file:
        for line in file.readlines():
            input.append(line.strip())
    
    return input

def vowel_count(input):
    res = 0
    
    for c in input:
        if c == 'a' or c == 'e' or c =='i' or c == 'o' or c == 'u':
            res += 1
    
    return True if res >= 3 else False

def appears_twice(input):
    res = 0
    for i in range(1, len(input)):
        if input[i] == input[i-1]:
            res += 1
    
    return True if res >= 1 else False

def does_not_contain(input):
    temp = ""
    for i in range(1, len(input)):
        temp += input[i-1] + input[i] 

        if temp == 'ab' or temp =='cd' or temp =='pq' or temp =='xy':
            return False
        
        temp = ""
    
    return True

def puzzle_1(input):
    res = 0
    for s in input:
        # print(s)
        temp = vowel_count(s) and appears_twice(s) and does_not_contain(s)
        if temp:
            res += 1
    
    
    # res = vowel_count(input) and appears_twice(input) and does_not_contain(input)
    print(f'The Puzzle 1 Solutions is: {res}') 

def has_repeated(input):
    hashmap = {}

    for i in range(len(input)-1):
        pair = input[i:i+2]
        if pair in hashmap:
            if i - hashmap[pair] > 1:
                return True
        else:
            hashmap[pair] = i
    
    return False

def has_repeated_between(input):
    for i in range(len(input) - 2):
        if input[i] == input[i+2]:
            return True
    
    return False

def puzzle_2(input):
    res = 0
    for s in input:
        # print(s)
        temp = has_repeated(s) and has_repeated_between(s)
        if temp:
            res += 1
    
    
    # res = vowel_count(input) and appears_twice(input) and does_not_contain(input)
    print(f'The Puzzle 2 Solutions is: {res}')  
    
    
if __name__ == "__main__":
    
    input = read_file()
    puzzle_1(input)
    puzzle_2(input)
    
    