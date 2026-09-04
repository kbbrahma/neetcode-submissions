class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0
        for n in nums:
            if n==1:
                current_count += 1
                max_count=max(max_count,current_count)
            else:
                if current_count > max_count:
                    max_count = max_count
                current_count = 0    
        return max(max_count, current_count)            


        