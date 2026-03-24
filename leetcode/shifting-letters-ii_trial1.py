class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
         n = len(s)
         diff = [0] * (n + 1)

         for l, r, d in shifts:
            val = 1 if d == 1 else -1
            diff[l] += val
            diff[r + 1] -= val

         for i in range(1, n):
            diff[i] += diff[i - 1]

         res = []
         for i in range(n):
            shift = diff[i] % 26
            new_char = (ord(s[i]) - ord('a') + shift) % 26
            res.append(chr(new_char + ord('a')))

         return "".join(res)