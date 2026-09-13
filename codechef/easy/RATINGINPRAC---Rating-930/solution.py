t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    # Your code goes here
    t -= 1
    c=1
    for i in range(1,n):
        if d[i-1]>=d[i]:
            c=0
            break
    if  c>0:
        print("YES")
    else:
        print("NO")
            