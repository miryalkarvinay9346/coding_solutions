# cook your dish here
l,r=map(int,input().split())
c=0
for i in range(l,r+1):
    if i%2==0:
        c=1
        break
print("YES" if c>0 else "NO")
        