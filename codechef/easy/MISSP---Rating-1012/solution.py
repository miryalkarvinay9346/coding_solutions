# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=[0]*n
    for i in range(n):
        a[i]=int(input())
    for j in a:
        if a.count(j)%2!=0:
            print(j)
            break