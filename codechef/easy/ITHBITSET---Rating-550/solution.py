class Solution:
    def isBitSet(self, n: int, i: int) -> bool:
        # write your code here 
        s=bin(n)[2:][::-1]
        return i<len(s) and s[i]=='1'