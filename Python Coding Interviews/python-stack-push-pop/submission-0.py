from typing import List

def stack_not_empty(arr: List[int]) -> bool: 
    if len(arr) != 0:
        return True
    else:
        return False

def stack_push(arr: List[int], item) -> None: 
    arr.append(item)

def stack_pop(arr: List[int]) -> int:
    if stack_not_empty(arr):
        return arr.pop()        



def reverse_list(arr: List[int]) -> List[int]:
    stack_arr = []
    for i in arr:
        stack_push(stack_arr, i)
    reverse_arr = []    
    while stack_not_empty(stack_arr):
        k = stack_pop(stack_arr)
        reverse_arr.append(k)
    return reverse_arr    



# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
