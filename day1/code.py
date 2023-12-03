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

if __name__ == "__main__":
    file = open(sys.argv[1]).read().strip()
    puzzle = Puzzle()
    
    result = puzzle.puzzle_1(file)
    print(f"The puzzle 1 value is: {result}")