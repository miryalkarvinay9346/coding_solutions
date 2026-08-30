t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    # your code goes here
    s.sort()
    m=float('inf')
    for i in range(1,n):
        k=abs(s[i]-s[i-1])
        m=min(k,m)
    print(m)