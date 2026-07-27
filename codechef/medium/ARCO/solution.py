# cook your dish here
n=int(input())
a=list(map(int,input().split()))
stack=[]
for i in a:
    if stack>0 and stack[-1]==i:
        stack.pop()
    else:
        stack.append(i)
print(len(stack))