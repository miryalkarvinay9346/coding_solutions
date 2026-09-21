# cook your dish here
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n-1):
    k=0
    if (a[i]==2*i-2 and a[i+1]==2*i) or (a[i]==2*n and a[i+1]==2*i-2):
        continue
    else:
        c+=1
print(c)