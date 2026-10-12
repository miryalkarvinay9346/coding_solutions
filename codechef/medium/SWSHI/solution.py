# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    if min(a)<m:
        print(0)
        continue
    c=0
    