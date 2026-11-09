# cook your dish here
for _ in range(int(input())):
    p,d,k,b=map(int,input().split())
    a=p+d*k
    if a<=b:
        print("YES")
    else:
        print("NO")