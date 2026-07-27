def add_two_numbers() -> int:
    nums = input().split(",")
    s = 0
    for n in nums:
        s+=int(n)
    return s    




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
