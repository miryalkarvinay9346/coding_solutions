# PEAKINARRAY1 - Rating 950

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Find the peak elements in an array

Given an array $A$ of size $n$, your task is to find and print all the peak elements in the array. A peak element is one that is strictly greater than its neighbouring elements. For the first and last elements, only consider their single adjacent element.

If no peak element exists in the array, print $-1$.

## Function Declaration
### Function Name

$findPeaks$ – This function finds and prints all  **peak elements**  in an array. A peak element is one that is strictly greater than its adjacent elements.

### Parameters
- $A$ : An array of integers.
- $n$ : An integer representing the size of the array.
### Return Value
- Return an array with all peak elements in the order they are present in the original array.
- Return $-1$ if no peak element exists in the array.
## Constaints:
- $2 \leq n \leq 10^5$
- $1 \leq A_i \leq 10^5$
### Input Format
- The first line contains the integer $n$ — the size of array
- The second line contains all the elements of array $A$
### Output Format

Output all the peak elements in the array in the order they are present in the original array.

### Sample 1:
Input
Output

```
5
1 2 4 3 1
```

```
4
```

### Explanation:

1 is smaller than it's adjacent element 2. Thus it's not a peak.
2 is greater than 1 but smaller than 4. Thus it's not a peak
4 is greater than both 2 and 3, thus it is a  **peak**  element.
Again 3 and 1 are also smaller than their adjacent elements. Thus it's not a peak
Thus the output is only 4.

### Sample 2:
Input
Output

```
5
7 3 5 2 10
```

```
7 5 10
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T04:55:36.749Z  

```py
def findPeaks(A: list[int], n: int) -> list[int]:
    # write your code here 
    a=[]
    for i in range(len(A)):
        if i==0:
            if A[i]>A[i+1]:
                a.append(A[i])
        elif i==len(A)-1:
            if A[i]>A[i-1]:
                a.append(A[i])
        else:
            if A[i]>A[i-1]  and A[i]>A[i+1] :
                a.append(A[i])
    if not a:
        return -1
    return a #if len(a)>0 else -1
```

---

[View on CodeChef](https://www.codechef.com/problems/PEAKINARRAY1)