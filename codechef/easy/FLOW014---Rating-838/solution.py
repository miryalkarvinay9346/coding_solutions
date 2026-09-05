# cook your dish here
for _ in range(int(input())):
    h,c,t=map(float,input().split())
    hard=(True if h>50 else False)
    carb=(True if c<0.7 else False)
    tens=(True if t>5600 else False)
    if hard and carb and tens:
        print(10)
    elif hard and carb:
        print(9)
    elif carb and tens:
        print(8)
    elif hard and tens:
        print(7)
    elif hard or carb or tens:
        print(6)
    else:
        print(5)
    