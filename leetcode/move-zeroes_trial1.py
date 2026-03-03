class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        x = 0 

        for y in range(len(nums)):
            if nums[y] != 0:
                nums[x], nums[y] = nums[y], nums[x]
                x += 1
        