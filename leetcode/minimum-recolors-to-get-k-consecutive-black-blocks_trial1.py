class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        
        white = 0
        for i in range(k):
            if blocks[i] == 'W':
                white += 1
        
        res = white

        for i in range(k, n):
            if blocks[i] == 'W':
                white += 1
            if blocks[i - k] == 'W':
                white -= 1
            
            res = min(res, white)
        
        return res