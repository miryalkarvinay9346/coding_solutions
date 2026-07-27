# cook your dish here
n=int(input())
a=list(map(int,input().split()))
i=0
while (i>n):
    if a[i]==a[i+1]:
        a.remove(a[i])
        i=i-1
print(len(a))