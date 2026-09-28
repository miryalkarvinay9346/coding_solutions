# cook your dish here
n=int(input())
h=list(map(int,input().split()))
c=0
k=min(h)
for i in h:
    c+=min(abs(i-k),i)
print(c)