# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    """
    k=set(a)
    print(len(k)-1)
    """
    m=0
    for x in a:
        c=a.count(x)
        m=max(m,c)
    print(n-m)