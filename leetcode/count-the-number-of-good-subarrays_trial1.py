class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left = 0
        freq = {}
        pairs = 0
        result = 0

        for right in range(len(nums)):
            num = nums[right]

            pairs += freq.get(num, 0)
            freq[num] = freq.get(num, 0) + 1
            
            while pairs >= k:
                result += len(nums) - right

                left_num = nums[left]
                freq[left_num] -= 1
                pairs -= freq[left_num]
                left += 1

        return result