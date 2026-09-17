t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    # your code goes here
    a.sort(reverse=True)
    k=min(a[:x])
    print(k-1)