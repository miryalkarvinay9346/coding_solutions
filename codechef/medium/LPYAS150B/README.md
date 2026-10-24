# LPYAS150B

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com

Write a program that accepts the count of test cases t, then for each test case, reads a string `s`, checks if it's a palindrome or not using the `check_palindrome` function, and outputs "YES" if `s` is palindrome, else "NO".

 **Note** : A string is palindrome if that reads the same backward or forward. For example string  **level**  is a palindrome.

### Sample 1:
Input
Output

```
3
amma
naman
hello
```

```
YES
YES
NO
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T05:43:23.800Z  

```py
def check_palindrome(s):
    # Complete the function
    if s==s[::-1]:
        return "YES"
    else:
        return "NO"
def main():
    test_cases = int(input())
    # Complete the function
    for _ in range(test_cases):
        s=input()
        k=check_palindrome(s)
        print(k)

main()
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS150B)