# cook your dish here
for _ in range(int(input())):
    x1,y2=map(int,input().split())
    k=""
    if y2==0:
        k+="1"*x1
    elif x1==0:
        k+="2"*y2
    else:
        k+="1"*(x1//2)
        k+="2"*y2
        k+="1"*(x1//2)
    print(k)
    