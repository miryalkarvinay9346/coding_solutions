# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=map(int,input().split())
    count=0
    for i in s:
        if(i<=4):
            count+=1
    if(count==0):
        print("yes")
    else:
        print("NO")