# cook your dish here
x = int(input())
for _ in range(x):
    a, b = map(int, input().split())
    required = 50 - a
    min_sum = 2 * b
    max_sum = 2 * b + 10
    if min_sum <= required <= max_sum:
        print("yes")
    else:
        print("no")