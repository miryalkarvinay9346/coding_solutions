class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1=str(bin(a)[2:]).count("1")
        s2=str(bin(b)[2:]).count("1")
        if s1>=s2:
            return s1*s2
        return s2//s1