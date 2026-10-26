# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    print("YES" if x==y and x>=1 and y>=1 else "NO")