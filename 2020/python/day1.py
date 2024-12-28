input_list = list(map(int, open("input.txt").read().splitlines()))

def two_sum(nums, target):
    hashmap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashmap:
            return [diff, n]
        hashmap[n] = i
    return None

def three_sum(nums, target):
    nums.sort()
    
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = a + nums[l] + nums[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return [a, nums[l], nums[r]]
    
    return None


if __name__ == "__main__":
    sample_input = [1721, 979, 366, 299, 675, 1456]
    val1, val2 = two_sum(input_list, 2020)
    res1 = val1 * val2
    print(f"Part 1: {res1}")
    
    val1, val2, val3 = three_sum(input_list, 2020)
    res2 = val1 * val2 * val3
    print(f"Part 2: {res2}")
    
