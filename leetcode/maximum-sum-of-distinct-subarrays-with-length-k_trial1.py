class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        current_sum = 0
        max_sum = 0
        freq = {}

        for right in range(len(nums)):
            num = nums[right]
            current_sum += num
            freq[num] = freq.get(num, 0) + 1

            if right - left + 1 > k:
                remove = nums[left]
                current_sum -= remove
                freq[remove] -= 1
                if freq[remove] == 0:
                    del freq[remove]
                left += 1

            if right - left + 1 == k and len(freq) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum