# cook your dish here
l=int(input())
b=int(input())
p=2*(l+b)
a=l*b
if p>a:
    print(f"Peri\n{p}")
elif p<a:
    print(f"Area\n{a}")
else:
    print(f"Eq\n{a}")