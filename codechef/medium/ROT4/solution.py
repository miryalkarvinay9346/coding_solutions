# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    c=0
    for i in range(n-1):
        k=int(str(int(s[i])+int(s[i+1])))
        if k%4==0:
            c+=1
        print(k)
    print(c)
            