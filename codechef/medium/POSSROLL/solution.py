# cook your dish here
x,k,y=map(int,input().split())
if y%k==0 and y<=x*k:
    print("YES")
else:
    print("NO")