# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    e=a[k-1]
    a.sort()
    print(a.index(e)+1)