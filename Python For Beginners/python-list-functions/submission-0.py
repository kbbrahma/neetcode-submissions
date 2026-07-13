from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    total_sum = 0
    for n in nums:
        total_sum += n
    return total_sum    

def get_min(nums: List[int]) -> int:
    minimum = nums[0]
    for n in nums:
        if n<minimum:
            minimum = n
    return minimum        

def get_max(nums: List[int]) -> int:
    maximum = nums[0]
    for n in nums:
        if n>maximum:
            maximum = n
    return maximum 

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
