# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    c=list(map(int,input().split()))
    a=100*100
    for i  in range(n):
        for j in range(i+1,n):
            if (i+1)-k>1:
                continue
            if (j+1)+k<n:
                print("J")
                continue
            else:
                if (j+1)+k>i+1-k+1:
                    print("K")
                    continue
            a=min(a,c[i]+c[j])
    if a==100*100:
        print(-1)
    else:
        print(a)