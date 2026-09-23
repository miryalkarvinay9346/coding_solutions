# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    cn=0
    cp=0
    """
    if sum(a)>=0:
        #print("YES")
    else:"""
    s=sum(a)
    c=0
    for i in range(n):
        if s-a[i]>=0:
            c=1
            break
    print("YES" if c else "NO")
            