# cook your dish here
n=int(input())
a=list(map(int,input().split()))
a.sort()
m=float('inf')
for i in range(n):
    if a[i]