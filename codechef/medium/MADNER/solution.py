class Solution:
    def findMaximumPairs(self, students: str) -> int:
        # write your code here
        m=0
        c=0
        #k=students[0]
        for i in range(len(students)-1):
            k=students[i]
            if (k=="x" and students[i+1]=="y") or (k=="y" and students[i+1]=="x") :
                c+=1
            else:
                c=0
                k=students[i]
            if c==1:
                m+=1
                i=i+2
        return m