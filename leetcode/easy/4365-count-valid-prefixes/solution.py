class Solution:
    def countValidPrefixes(self, s: str) -> int:
        c0,c1,c=0,0,0
        for i in range(len(s)):
            if s[i]=="0":
                c0=c0+1
            else:
                c1=c1+1
            if abs(c0-c1)<=1:
                c+=1
        return c
        