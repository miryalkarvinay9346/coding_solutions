# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    k=x*3
    if k>=y:
        print("YES")
    else:
        print("NO")