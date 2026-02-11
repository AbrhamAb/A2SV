class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []

        for i in range(len(nums)):
            if nums[i] < 0:
                current = -nums[i]
            else:
                current = nums[i]

            index = current - 1

            if nums[index] < 0:
                duplicates.append(current)
            else:
                nums[index] = -nums[index]

        return duplicates
