# cook your dish here
for _ in range(int(input())):
    a1,a2,a3,a4,a5=map(int,input().split())
    l60=0
    l30=0
    k=[a1,a2,a3,a4,a5]
    for i in k:
        if i>=60:
            l60+=1
        if i>=30:
            l30+=1
    if l60>=2 and l30>=4:
        print("Pass")
    else:
        print("Fail")