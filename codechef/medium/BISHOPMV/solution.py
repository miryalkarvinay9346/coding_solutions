# cook your dish here
for _ in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    if x1==x2 and y1==y2:
        print(0)
    elif abs(x1-x2)==abs(y1-y2):
        print(1)
    elif (x1+y1)%2!=(x2+y2)%2:
        print(-1)
    else:
        print(2)