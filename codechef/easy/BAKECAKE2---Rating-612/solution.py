# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cost = 0
    for i in range(n):
        if a[i] > b[i]:
            cost += a[i] - b[i]
    print(cost)
