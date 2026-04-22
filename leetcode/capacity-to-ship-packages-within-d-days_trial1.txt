class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap):
            d = 1
            current = 0
            
            for w in weights:
                if current + w > cap:
                    d += 1
                    current = 0
                current += w
            
            return d <= days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1

        return left