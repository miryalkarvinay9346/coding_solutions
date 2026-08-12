def findLargestOddSubstring(num):
    # write your code here...
    a=num[::-1]
    c=-1
    for i in range(len(a)):
        if int(a[i])%2!=0:
            c=i
            break
    if c>=0:
        p=a[c::]
        return (p[::-1])
    else:
        return (c)
            
    