class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4

        mp = {'Q': 0, 'W': 1, 'E': 2, 'R': 3}
        count = [0] * 4

        for c in s:
            count[mp[c]] += 1

        if all(count[i] == target for i in range(4)):
            return 0
        
        res = n
        left = 0
        
        for right in range(n):
            count[mp[s[right]]] -= 1

            while left < n and all(count[i] <= target for i in range(4)):
                res = min(res, right - left + 1)
                count[mp[s[left]]] += 1
                left += 1
        
        return res