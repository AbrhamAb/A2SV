class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        target_positions = []
        
        for index, value in enumerate(nums):
            if value == target:
                target_positions.append(index)
        
        return target_positions