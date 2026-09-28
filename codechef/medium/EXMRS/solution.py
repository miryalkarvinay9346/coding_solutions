# cook your dish here
c,m,w,p,r=map(int,input().split())
t=c*m-w*p
print("YES" if t>=r else "NO")