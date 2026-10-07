# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    s=input()
    l=input()
    cl=0
    cr=0
    for i in range(m):
        if s[i] in l :
            cl=cl+1
        else:
            cr+=1
    print(max(cl,cr))