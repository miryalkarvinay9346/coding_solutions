# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    c=0
    k=0
    for i in range(n-1):
        if c==3:
            k=k+1
        if s[i]==s[i+1]:
            c+=1
        else:
            c=0
    print(k)
            