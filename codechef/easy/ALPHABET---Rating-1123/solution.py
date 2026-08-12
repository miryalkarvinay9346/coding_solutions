# cook your dish here
s=input()
n=int(input())
for _ in range(n):
    w=input()
    c=1
    for i in w:
        if i not in s:
            c=0
            break
    print("Yes" if c else "No")
