# cook your dish here
x,y,z=map(int,input().split())
print("YES" if x+y*0.5 +(4-(x+y+z))>y*0.5+z else "NO")