class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []

        for num in arr2:
            for x in arr1:
                if x == num:
                    result.append(x)

        rest = []
        for x in arr1:
            if x not in arr2:
                rest.append(x)

        rest.sort()

        return result + rest
        