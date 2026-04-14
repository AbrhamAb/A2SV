class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            curr = nums[i % n]

            while stack and nums[stack[-1]] < curr:
                res[stack.pop()] = curr

            if i < n:
                stack.append(i)

        return res