# cook your dish here
n,c=map(int,input().split())
a=list(map(int,input().split()))
print("YES" if sum(a)<=c else "NO")