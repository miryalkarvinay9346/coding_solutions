class Solution:
    def isPalindromic(self, s: str) -> bool:
        k=""
        for i in range(len(s)):
            a=ord(s[i])
            #m=format(a,"08b")
            m=bin(a)[2:].zfill(8)
            k=k+m
        return k==k[::-1]