# cook your dish here
for _ in range(int(input())):
    s=input()
    r=input()
    m=[""]*5
    for i in range(5):
        if s[i]==r[i]:
            m[i]="G"
        else:
            m[i]="B"
    print("".join(m))