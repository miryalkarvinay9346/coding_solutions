# PYTHCL61A

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program that takes 3 string inputs from the user: a `name`, a `verb`, and a `place`. Use these inputs to construct a sentence in the following format:

`"<name> is <verb> in the <place>"`

### Sample 1:
Input
Output

```
Alice dancing park
```

```
Alice is dancing in the park
```

### Sample 2:
Input
Output

```
Rohan chilling club
```

```
Rohan is chilling in the club
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T16:49:38.258Z  

```py
# Update the code below this line.
n=input().split()
s=""
c=0
for i in n:
    c+=1
    s+=i+" "
    if c==1:
        s+="is "
    if c==2:
        s+="in the "
print(s[:len(s)])
    


```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHCL61A)