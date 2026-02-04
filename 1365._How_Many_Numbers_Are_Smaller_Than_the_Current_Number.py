class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        count = [0] * 101
        for x in nums:
            count[x] += 1

        for i in range(1, 101):
            count[i] += count[i - 1]

        result = []
        for x in nums:
            result.append(count[x - 1] if x > 0 else 0)

        return result
