import sys
from collections import defaultdict

class Puzzle:
    def puzzle_1(self, file):
        result = 0
        for line in file.split('\n'):
            flag = True
            id_, line = line.split(':')
            temp = defaultdict(int)
            
            for event in line.split(';'):
                for balls in event.split(','):
                    n, color = balls.split()
                    n = int(n)
                    temp[color] = max(temp[color], n)
                    
                    if int(n) > {'red':12, 'green':13, 'blue':14}.get(color, 0):
                        flag = False
            score = 1
            for t in temp.values():
                score *= t
            
            if flag:
                result += int(id_.split()[-1])
        
        return result
    
if __name__ == "__main__":
    file = open(sys.argv[1]).read().strip()
    puzzle = Puzzle()
    result = puzzle.puzzle_1(file)
    print(f"The Puzzle 1 answer: {result}")