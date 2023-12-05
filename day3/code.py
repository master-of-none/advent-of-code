import sys
import re
from collections import defaultdict

class Puzzle:
    def puzzle_1(self, file):        
        lines = file.split('\n')
        graph = [[c for c in line] for line in lines]
        rows = len(graph)
        cols = len(graph[0])
        
        result = 0
        nums = defaultdict(list)
        for r in range(len(graph)):
            gears = set()
            n = 0
            flag = False
            
            for c in range(len(graph[r]) + 1):
                if c < cols and graph[r][c].isdigit():
                    n = n * 10 + int(graph[r][c])
                    
                    for rr in [-1, 0, 1]:
                        for cc in [-1, 0, 1]:
                            if 0 <= r + rr < rows and 0 <= c + cc < cols:
                                ch = graph[r + rr][c + cc]
                                
                                if not ch.isdigit() and ch != '.':
                                    flag = True
                                
                                if ch == '*':
                                    gears.add((r + rr, c + cc))
                
                elif n > 0:
                    for gear in gears:
                        nums[gear].append(n)
                    
                    if flag:
                        result += n
                    
                    n = 0
                    flag = False
                    gears = set()
        
        return result
    
    def puzzle_2(self, file):        
        lines = file.split('\n')
        graph = [[c for c in line] for line in lines]
        rows = len(graph)
        cols = len(graph[0])
        
        result = 0
        nums = defaultdict(list)
        for r in range(len(graph)):
            gears = set()
            n = 0
            flag = False
            
            for c in range(len(graph[r]) + 1):
                if c < cols and graph[r][c].isdigit():
                    n = n * 10 + int(graph[r][c])
                    
                    for rr in [-1, 0, 1]:
                        for cc in [-1, 0, 1]:
                            if 0 <= r + rr < rows and 0 <= c + cc < cols:
                                ch = graph[r + rr][c + cc]
                                
                                if not ch.isdigit() and ch != '.':
                                    flag = True
                                
                                if ch == '*':
                                    gears.add((r + rr, c + cc))
                
                elif n > 0:
                    for gear in gears:
                        nums[gear].append(n)
                    
                    if flag:
                        pass
                    
                    n = 0
                    flag = False
                    gears = set()
        
        for k, v in nums.items():
            if len(v) == 2:
                result += v[0] * v[1]
        
        return result
        
if __name__ == "__main__":
    file = open(sys.argv[1]).read().strip()
    puzzle = Puzzle()
    result1 = puzzle.puzzle_1(file)
    print(f"The result of puzzle 1 is: {result1}")
    
    result2 = puzzle.puzzle_2(file)
    print(f"The result of the puzzle 2 is: {result2}")