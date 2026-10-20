# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    sil=0
    pu=0
    for i in s:
        if i=="0":
            sil=1
        elif i=="1"and sil==1:
            pu+=1
    print(pu)