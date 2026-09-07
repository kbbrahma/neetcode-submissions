class Solution:
    #O(n)
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        n = len(arr)
        for i in range(n-1,-1,-1):
            new_max = max(right_max,arr[i])
            arr[i] = right_max
            right_max = new_max
        return arr    
        
        