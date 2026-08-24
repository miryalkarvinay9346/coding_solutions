# cook your dish here
s=input().lower()
a=[]
for i in range(len(s)):
    c=0
    for j inn range(len(s)):
        if s[i]==s[j] and s[i].isalpha():
            c+=1
    a.append(c)
