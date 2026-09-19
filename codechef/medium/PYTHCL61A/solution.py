# Update the code below this line.
n=input().split()
s=""
c=0
for i in n:
    c+=1
    s+=i+" "
    if c==1:
        s+="is "
    if c==2:
        s+="in the "
print(s[:len(s)])
    

