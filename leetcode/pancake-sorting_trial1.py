class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        n = len(arr)

        for target in range(n, 1, -1):
            idx = arr.index(target)
            if idx != target - 1:
                if idx != 0:
                    flips.append(idx + 1)
                    arr[:idx+1] = arr[:idx+1][::-1]
                flips.append(target)
                arr[:target] = arr[:target][::-1]

        return flips