t = int(input())

while t > 0:
    n, x = map(int, input().split())
    # Your code goes here
    if len(str(n*x))==5:
        print("YES")
    else:
        print("NO")
    t -= 1
