class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        wmap = {}
        ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for l in ABC:
            wmap[l] = 0
        def get_max():
            maxl = 0
            let = ""
            for l in ABC:
                if wmap[l] > maxl:
                    maxl = wmap[l]
                    let = l
            return let
        l = 0


        for r in range(len(s)):
            wmap[s[r]] += 1

            while wmap[get_max()] + k < r - l + 1:
                wmap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1) 

        return res
        