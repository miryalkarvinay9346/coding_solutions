class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        a=[words[0]]
        for i in range(1,len(words)):
            if sorted(words[i])!=sorted(a[-1]):
                a.append(words[i])
        return a