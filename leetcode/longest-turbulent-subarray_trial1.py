class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n
        
        max_len = 1
        curr_len = 1
        
        prev = 0 
        
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                curr = 1
            elif arr[i] < arr[i - 1]:
                curr = -1
            else:
                curr = 0
            
            if curr == 0:
                curr_len = 1
            elif curr * prev == -1:
                curr_len += 1
            else:
                curr_len = 2
            
            max_len = max(max_len, curr_len)
            prev = curr
        
        return max_len