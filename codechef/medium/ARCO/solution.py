# cook your dish here
n=int(input())
a=list(map(int,input().split()))
for i in range(n-1):
    if a[i]==a[i+1]:
        a.remove(a[i+1])
print(len(a))