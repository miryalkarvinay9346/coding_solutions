# cook your dish here
for _ in range(int(input())):
    q,p=map(int,input().split())
    if q>1000:
        k=p-(p*0.1)
        print(f"{k*q:.6f}")
    else:
        print(f"{p*q:.6f}")