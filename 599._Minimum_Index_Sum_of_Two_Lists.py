class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        position = {}
        for i in range(len(list1)):
            position[list1[i]] = i

        result = []
        min_sum = 10**9

        for j in range(len(list2)):
            if list2[j] in position:
                total = position[list2[j]] + j

                if total < min_sum:
                    min_sum = total
                    result = [list2[j]]
                elif total == min_sum:
                    result.append(list2[j])

        return result
