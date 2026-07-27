# cook your dish here
n=int(input())
a=list(map(int,input().split()))
k=[]
for i in a:
    if k==True and k[-1]==i:
        k.pop()
    else:
        k.append(i)
print(len(k))