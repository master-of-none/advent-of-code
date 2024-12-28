import hashlib

def puzzle_1(secret_key):
    number = 1
    
    while True:
        input_string = secret_key + str(number)
        
        hash_result = hashlib.md5(input_string.encode()).hexdigest()
        
        if hash_result.startswith('00000'):
            return number

        number += 1

def puzzle_2(secret_key):
    number = 1
    
    while True:
        input_string = secret_key + str(number)
        
        hash_result = hashlib.md5(input_string.encode()).hexdigest()
        
        if hash_result.startswith('000000'):
            return number

        number += 1

if __name__ == "__main__":
    secret_key = "ckczppom"
    res1 = puzzle_1(secret_key)
    print(f'The Puzzle 1 Solution is: {res1}')
    
    res2 = puzzle_2(secret_key)
    print(f'The Puzzle 1 Solution is: {res2}')