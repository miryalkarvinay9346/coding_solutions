# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    if k>n:
        print(sum(a))
    else:
        print(sum(a[:k+1]))