class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        
        window_size = 2 * k + 1
        
        if window_size > n:
            return res
            
        curr_sum = sum(nums[:window_size])
        res[k] = curr_sum // window_size
        
        for i in range(window_size, n):
            curr_sum += nums[i] - nums[i - window_size]
            res[i - k] = curr_sum // window_size
        
        return res