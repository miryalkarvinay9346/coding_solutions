class Solution:
    def minimumSum(self, num: int) -> int:
        k=str(num)
        a=[int(k[0]),int(k[1]),int(k[2]),int(k[3])]
        a.sort()
        s1=int(str(a[0])+str(a[2]))
        s2=int(str(a[1])+str(a[3]))
        return s1+s2