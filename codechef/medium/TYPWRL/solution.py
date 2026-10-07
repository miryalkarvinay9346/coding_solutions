# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    s=input()
    l=input()
    cl=0
    cr=0
    k=0
    for i in range(n):
        if s[i] in l :
            cl=cl+1
            cr=0
        else:
            cr+=1
            cl=0
        k=max(cl,cr)
    print(k)