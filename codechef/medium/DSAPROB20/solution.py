def largestCommonElement(arr1, arr2):
    # Write your code here
    arr1.sort(reverse=True)
    #arr2.sort(reverse=True)
    #n,m=len(arr1),len(arr2)
    #k=min(n,m)
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            return (arr1[i])
    return -1       