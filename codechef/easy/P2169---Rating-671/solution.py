# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    t=""
    for i in s:
        if i=="1":
            t+="0"
        else:
            t+="1"
    print(t)