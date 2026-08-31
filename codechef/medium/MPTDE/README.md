# MPTDE

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Minimum Potions

A warrior is travelling along a path guarded by $N$ enemies, which must be encountered in the given order. He begins the journey with $S$ stamina.

The $i$-th enemy requires $cost_i$ stamina to defeat. If the warrior has at least $cost_i$ stamina, he may defeat that enemy, after which his stamina decreases by $cost_i$.

To continue fighting, the warrior carries magical potions. Before fighting an enemy, he may use a potion to restore his stamina to exactly $S$. There is no limit on the number of potions he may use.

The warrior may also choose to  **skip**  an enemy instead of fighting it. Skipping does not consume any stamina, but he may skip at most $K$ enemies throughout the journey.

Each enemy must be handled in order, either by defeating it or skipping it.

Find the  **minimum number of potions**  the warrior must use to get past all $N$ enemies.

If it is impossible to do so while skipping at most $K$ enemies, print `-1`.

### Input Format
- The first line contains three integers $N$, $S$, and $K$ — the number of enemies, maximum stamina, and maximum number of enemies that may be skipped.
- The second line contains $N$ space-separated integers $cost_1,cost_2,\ldots,cost_N$, where $cost_i$ is the stamina required to defeat the $i$-th enemy.
### Output Format
- Print a single integer — the minimum number of potions required to get past all $N$ enemies.
- If it is impossible to process all enemies while skipping at most $K$ of them, print -1.
### Constraints
- $1 \le N \le 10^3$
- $1 \le S \le 1000$
- $0 \le K \le N$
- $1 \le cost_i \le 1000$
### Sample 1:
Input
Output

```
5 10 1
4 6 8 2 5
```

```
1
```

### Explanation:

The warrior defeats the first two enemies, reducing his stamina from `10` to `0`. He then skips the third enemy and uses one potion to restore his stamina to `10`. After defeating the fourth and fifth enemies, he is left with `3` stamina.

Therefore, the warrior can get past all the enemies using only  **one potion**.

### Sample 2:
Input
Output

```
4 5 1
6 2 7 1
```

```
-1
```

### Explanation:

The warrior starts with $5$ stamina.

The enemies requiring `6` and `7` stamina cannot be defeated even after using a potion, since a potion restores the stamina only to $5$.

Therefore, both enemies would have to be skipped.

Since the warrior can skip at most $1$ enemy, it is impossible to get past all the enemies.

Hence, the output is `-1`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-31T14:02:16.734Z  

```py
# cook your dish here

```

---

[View on CodeChef](https://www.codechef.com/problems/MPTDE)