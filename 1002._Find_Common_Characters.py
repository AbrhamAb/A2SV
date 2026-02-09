class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common = list(words[0])
        
        for w in words[1:]:
            temp = []
            for ch in common:
                if ch in w:
                    temp.append(ch)
                    w = w.replace(ch, '', 1)
            common = temp
        
        return common
