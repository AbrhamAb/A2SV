class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        for i in range(len(nums) - k + 1):
            mx = nums[i]
            
            for j in range(i, i + k):
                if nums[j] > mx:
                    mx = nums[j]
            
            res.append(mx)
        
        return res