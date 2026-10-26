# cook your dish here
s=input()
a=""
i=0
while i<len(s):
    if i<len(s)-1 and s[i+1]=="#":
        k=s[i]
        a=a+chr(ord('o')+ord("z")-ord(k))
        i+=2
    else:
        k=s[i]
        a+=chr(ord("a")+ord("n")-ord(k))
print(a)