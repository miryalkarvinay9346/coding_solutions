# cook your dish here
for _ in range(int(input())):
    a1,a2,b1,b2=map(int,input().split())
    if (a1-a2)+(b1-b2)<0:
        print("YES")
    else:
        print("NO")