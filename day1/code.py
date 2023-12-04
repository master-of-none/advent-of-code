import sys
class Puzzle:
    def puzzle_1(self, file):
        result = 0
        for line in file.split('\n'):
            digits = []
    
            for c in line:
                if c.isdigit():
                    digits.append(c)
            
            temp = int(digits[0]+digits[-1])
            result += temp
        
        return result

    def puzzle_2(self, file):
        p1 = 0
        p2 = 0
        
        for line in file.split('\n'):
            p1_digits = []
            p2_digits = []
            
            for i, c in enumerate(line):
                if c.isdigit():
                    p1_digits.append(c)
                    p2_digits.append(c)
                    
                for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                    if line[i:].startswith(val):
                        p2_digits.append(str(d+1))
                
            p1 += int(p1_digits[0] + p1_digits[-1])
            p2 += int(p2_digits[0] + p2_digits[-1])
            
        return p1, p2 
        
if __name__ == "__main__":
    file = open(sys.argv[1]).read().strip()
    puzzle = Puzzle()
    
    result = puzzle.puzzle_1(file)
    print(f"The puzzle 1 value is: {result}")
    result1, result2 = puzzle.puzzle_2(file)
    print(f"The puzzle 2 value is: {result1} {result2}")