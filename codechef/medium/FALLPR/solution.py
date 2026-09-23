# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        if sum(a[:i])+sum(a[i+1:])>=0:
            continue
        else:
            c=1
            break
    print("YES" if c else "NO")
            