# cook your dish here
for i in range(int(input())):
    n = int(input())
    pos = n
    for j in range(1, n):
        if j % 2 == 1:
            pos -= n - j
        else:
            pos += n - j
    print(pos)