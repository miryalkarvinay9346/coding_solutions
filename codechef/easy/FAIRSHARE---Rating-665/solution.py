# cook your dish here
def fss(n,m,ans):
    s=n//(m+1)
    ans=(n-(s*m))
    return ans
    
for _ in range(int(input())):
    n,m=map(int,input().split())
    ans=0
    k=fss(n,m,ans)
    print(k)