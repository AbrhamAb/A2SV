class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        result = []
        for x in nums:
            result.append(x)
        for x in nums:
            result.append(x)
        return result
