import sys
import re
from collections import defaultdict

class Puzzle:
    def puzzle_1(self, file):
        lines = file.split('\n')
        result = 0
        hashmap = defaultdict(int)
        
        for i, line in enumerate(lines):
            hashmap[i] += 1
            head, tail = line.split('|')
            id_, card = head.split(':')
            card_num = [int(x) for x in card.split()]
            tail_num = [int(x) for x in tail.split()]
            
            val = len(set(card_num) & set(tail_num))
            
            if val > 0:
                result += 2 ** (val - 1)
            
            for j in range(val):
                hashmap[i + 1 + j] += hashmap[i]
            
        return result 
    
    def puzzle_2(self, file):
        lines = file.split('\n')
        result = 0
        hashmap = defaultdict(int)
        
        for i, line in enumerate(lines):
            hashmap[i] += 1
            head, tail = line.split('|')
            id_, card = head.split(':')
            card_num = [int(x) for x in card.split()]
            tail_num = [int(x) for x in tail.split()]
            
            val = len(set(card_num) & set(tail_num))
            
            if val > 0:
                result += 2 ** (val - 1)
            
            for j in range(val):
                hashmap[i + 1 + j] += hashmap[i]
            
        return (sum(hashmap.values())) 
     
        
if __name__ == "__main__":
    file = open(sys.argv[1]).read().strip()
    puzzle = Puzzle()
    result1 = puzzle.puzzle_1(file)
    print(f"The puzzle 1 solution is: {result1}")
    
    result2 = puzzle.puzzle_2(file)
    print(f"The puzzle 2 solution is: {result2}")