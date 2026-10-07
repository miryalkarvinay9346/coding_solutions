# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    # U D L R
    x=s.count("U")-s.count("D")
    y=s.count("L")-s.count("R")
    if x==2 and y==0:
        print("YES")
    elif x==-2 and y==0:
        print("YES")
    elif x==0 and y==2:
        print("YES")
    elif x==0 and y==-2:
        print("YES")
    else:
        print("NO")