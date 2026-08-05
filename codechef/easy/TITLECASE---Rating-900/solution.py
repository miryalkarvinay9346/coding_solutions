# cook your dish here
import string
for _ in range(int (input())):
    s=input().split()
    for i in range(len(s)):
        if not s[i].isupper():
            s[i]=s[i].capitalize()
    print(" ".join(s))