# cook your dish here
for _ in range(int(input())):
    a,b,p,q,r=map(int,input().split())
    if a==b:
        print(r*a)
    else:
        c=0
        c+=((a//2)+a%2)*p
        c+=((b//2)+b%2)*q
        print(c)