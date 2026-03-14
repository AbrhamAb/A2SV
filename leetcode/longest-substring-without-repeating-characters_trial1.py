class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        start = 0
        max_length = 0

        for i, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= start:
                start = last_seen[ch] + 1

            last_seen[ch] = i
            max_length = max(max_length, i - start + 1)

        return max_length