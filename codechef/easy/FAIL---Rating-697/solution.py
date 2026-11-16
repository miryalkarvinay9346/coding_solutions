# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    c=0
    for i in range(n):
        s=s+a[i]
        if s//(i+1)<40:
            c=1
            break
            
    print("Yes" if c==0 else "No")