class Solution:
    def isBalanced(self, num: str) -> bool:
        es,os=0,0
        for i in range(len(num)):
            if i%2==0:
                es+=int(num[i])
            else:
                os+=int(num[i])
        return es==os
