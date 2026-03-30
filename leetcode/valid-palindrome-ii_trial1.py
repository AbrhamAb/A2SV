class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_pal(x):
            return x == x[::-1]
        
        if is_pal(s):
            return True

        for i in range(len(s)):
            new_s = s[:i] + s[i+1:]
            if is_pal(new_s):
                return True

        return False