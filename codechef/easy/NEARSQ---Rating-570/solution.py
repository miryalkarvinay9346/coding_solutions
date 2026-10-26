# cook your dish here
for _ in range(int(input())):
    n=int(input())
    """
    c=1
    for i in range(1,n+1):
        k=i*i
        c=max(c,k)
        if c>n:
            print((i-1)*(i-1))
            break
    """ 
    for i in range(n,0,-1):
        if n>=i*i:
            print(i*i)
            break