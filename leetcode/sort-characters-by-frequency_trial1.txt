class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        chars = sorted(freq, key=lambda x: freq[x], reverse=True)

        result = ""
        for c in chars:
            result += c * freq[c]

        return result