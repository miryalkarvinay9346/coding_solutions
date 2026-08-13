# SPC2025 - Rating 467

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### New-Pro Coder

 *Hola a todos, espero que todo vaya bien!!* 

Ved claims to be a pro at programming, but his friend Varun disagrees. To settle the debate, they decided to seek advice from their mentor. The mentor proposed a simple challenge:

Ved must write a program containing $N$ lines of code. When the code is compiled, the compiler will indicate how many of those lines have errors, denoted as $M$. Based on the results:

- If errors are present in at least half of the total lines, Ved will be labeled as a $\text{NEWBIE}$.
- Otherwise, he will be called a $\text{PRO}$

After compiling Ved's code, the compiler reported errors in $M$ lines. Determine Ved's skill category based on this evaluation.

### Input Format
- The input contains two space-separated integers $N$ and $M$ — the number of lines of code written by Ved and the number of lines of code containing errors, respectively.
### Output Format

Output $\text{PRO}$ if Ved is pro, else output $\text{NEWBIE}$.

It is allowed to print each character in either case. $\text{pro}, \text{pRo}, \text{PRo}$ will all be accepted.

### Constraints
- $1 \leq N \leq 1000$
- $1 \leq M \leq 1000$
- $M \leq N$
### Sample 1:
Input
Output

```
10 6
```

```
NEWBIE
```

### Explanation:

There were $10$ lines and Ved has errors in $6$ of them. Since $6 \ge 5$, where $5$ is half of $10$, Ved is a newbie due to having errors in at least half the lines.

### Sample 2:
Input
Output

```
9 4
```

```
PRO
```

### Explanation:

Half of $9$ is $4.5$. Ved has errors in less than half the lines, thus he is a pro.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-13T16:33:06.038Z  

```py
# cook your dish here
n,m=map(int,input().split())

```

---

[View on CodeChef](https://www.codechef.com/problems/SPC2025)