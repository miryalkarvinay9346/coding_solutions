t = int(input())

while t > 0:
    n = int(input())
    a = list(set(list(map(int, input().split()))))
    t -= 1
    # Your code goes here
    a.sort(reverse=True)
    print(a[0]+a[1])