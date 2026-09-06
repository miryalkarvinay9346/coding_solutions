# cook your dish here
for _ in range(int(input())):
    s=list(input())
    c=0
    #print(str(int(n)+1))
    for i in range(len(s)-1,-1,-1):
        if s[i]!="9":
            s[i]=str(int(s[i])+1)
            print("".join(s))
            c=1
            break
        s[i]="0"
    if not c:
        print("1"+"".join(s))