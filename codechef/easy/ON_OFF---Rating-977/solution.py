t = int(input())
while t > 0:
    n = int(input())
    s = input()
    r = input()
    # Your code goes here
    c=0
    for i in range(n):
        if s[i]!=r[i]:
            c+=1
    print("1" if c%2==0 else "0")
    t -= 1
