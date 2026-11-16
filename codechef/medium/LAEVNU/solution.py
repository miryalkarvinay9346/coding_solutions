# cook your dish here
s=input()
a=[]
for i in s:
    if i.isdigit():
        a.append(i)
if len(a)==0:
    print(-1)
else:
    e=[]
    for i in a:
        if int(i)%2==0:
            e.append(i)
    if len(e)==0:
        print(-1)
    else:
        if e.count("0")==len(e):
            print(0)
        else:
            se=min(e)
            a.remove(se)
            a.sort(reverse=True)
            a.append(se)
            print("".join(a))