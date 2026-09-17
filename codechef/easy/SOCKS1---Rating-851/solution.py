# cook your dish here
a,b,c=map(int,input().split())
k=True if a==b or b==c or (c==a) else False
print("YES" if k else "NO")