class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        for _,n in enumerate(nums):
            if n != val:
                nums[i] = n
                i+=1
            else:
                continue
        return i         
        