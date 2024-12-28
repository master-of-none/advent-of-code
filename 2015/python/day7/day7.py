from collections import defaultdict
import re

def parse_instructions(instructions):
    circuit = {}
    for line in instructions:
        parts = line.strip().split(" -> ")
        circuit[parts[1]] = parts[0]
    
    return circuit

def get_signal(wire, circuit, cache):
    if wire.isdigit():
        return int(wire)
    
    if wire in cache:
        return cache[wire]
    
    instruction = circuit[wire]
    
    if "AND" in instruction:
        a, b = instruction.split(" AND ")
        signal = get_signal(a, circuit, cache) & get_signal(b, circuit, cache)
        
    elif "OR" in instruction:
        a,b = instruction.split(" OR ")
        signal = get_signal(a, circuit, cache) | get_signal(b, circuit, cache)
    
    elif "LSHIFT" in instruction:
        a,b = instruction.split(" LSHIFT ")
        signal = get_signal(a, circuit, cache) << int(b)
    
    elif "RSHIFT" in instruction:
        a,b = instruction.split(" RSHIFT ")
        signal = get_signal(a, circuit, cache) >> int(b)
    
    elif "NOT" in instruction:
        _, a = instruction.split("NOT ")
        signal = ~get_signal(a, circuit, cache) & 0xFFFF
    else:
        signal = get_signal(instruction, circuit, cache)
    
    cache[wire] = signal
    return signal

def puzzle_1():
    with open("input.txt", "r") as file:
        instructions = file.readlines()
    
    circuit = parse_instructions(instructions)
    cache = {}
    return get_signal("a", circuit, cache)

if __name__ == "__main__":
    res1 = puzzle_1()
    print(f"The Puzzle 1 Solution is {res1}")
    
    