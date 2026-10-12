# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    c=list(map(int,input().split()))
    c.sort(reverse=True)
    print(sum(c[:k]))