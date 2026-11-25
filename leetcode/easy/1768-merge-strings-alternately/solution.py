class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        k=""
        n=len(word1)
        m=len(word2)
        for i in range(min(m,n)):
            k+=word1[i]+word2[i]
        if m>n:
            k+=word2[i+1:]
        elif m<n:
            k+=word1[i+1:]
        return k