# cook your dish here
for _ in range(int(input())):
    n=int(input())
    """
    for i in range(1, n + 1):
        if i * i > n:
            print((i - 1) * (i - 1))
            break
    else:
        print(n * n)
    """ 
    for i in range(n,0,-1):
        if n>=i*i:
            print(i*i)
            break