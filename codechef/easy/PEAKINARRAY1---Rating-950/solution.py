def findPeaks(A: list[int], n: int) -> list[int]:
    # write your code here 
    a=[]
    c=1
    p=A[0]
    for i in range(len(A)):
        if i==0:
            if p>A[i+1]:
                a.append(p)
        elif i==len(A)-1:
            if A[i]>A[i-1]:
                a.append(A[i])
        else:
            if A[i]>A[i-1]  and A[i]>A[i+1] :
                a.append(A[i])
    return a if len(a)>0 else -1