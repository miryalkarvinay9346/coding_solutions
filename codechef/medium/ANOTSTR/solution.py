# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    if a==b:
        print("YES")
    elif a.count("1")%2==b.count("1")%2  :#:and a.count("1")==b.count("1"):
        print("YES")
    else:
        print("NO")