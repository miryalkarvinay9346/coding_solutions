# CHOLY - Rating 641

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chess Olympiad

The $45$-th FIDE Chess Olympiad is currently being held in Budapest, Hungary.

Every round, teams of four players each face off against each other in four individual games.
A team receives $1$ point for winning a game, $0.5$ points for a draw, and $0$ points for a loss.

A team is said to  *win*  the round if they receive  **strictly**  more points than the opposing team.

In the current round, your favorite team has already won $X$ games, drawn $Y$ games, and lost $Z$ games.
Can they still win this round?

### Input Format
- The first and only line of input will contain three space-separated integers $X, Y,$ and $Z$ — the number of wins, draws, and losses so far.
### Output Format

Print a single string: either `"YES"` or `"NO"` (without quotes), denoting whether your team can still win the round.

Each character of the output may be printed in either uppercase or lowercase, i.e, the strings `NO`, `No`, `nO`, and `no` will all be treated as equivalent.

### Constraints
- $0 \leq X, Y, Z \leq 4$
- $X+Y+Z \leq 4$
### Sample 1:
Input
Output

```
1 1 0

```

```
Yes

```

### Explanation:

With one game won and one drawn, the team has $1+0.5 = 1.5$ points already, while their opponent has $0 + 0.5 = 0.5$.
There are two games remaining - if they win both, they will receive another two points while their opponent receives $0$, making the final scoreline $3.5$ to $0.5$ and hence a team victory.

### Sample 2:
Input
Output

```
2 0 2

```

```
No
```

### Explanation:

With two wins and two losses, both teams are on $2$ points.
There are no games remaining, so it's not possible for us to have  **strictly**  more points than the opposition.

### Sample 3:
Input
Output

```
0 1 1

```

```
Yes
```

### Explanation:

With one draw and one loss, we have $0.5$ points while the opponent has $1.5$.
However, if our team wins both remaining games, they'll end up on $2.5$ points while the opponent will stay on $1.5$, and hence our team wins the round.

### Sample 4:
Input
Output

```
0 2 1

```

```
No

```

### Explanation:

We have $0.5 + 0.5 = 1$ point, while the opponent has $0.5 + 0.5 + 1 = 2$ points.
There is one game left, even if we win it and receive $1$ point, the score will be $2$ points each.
Since our score is not  *strictly*  greater than the opponent's score, we can't win the round.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-29T18:48:46.089Z  

```py
# cook your dish here
x,y,z=map(int,input().split())
print("YES" if x+y*0.5 +(4-(x+y+z))>y*0.5+z else "NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/CHOLY)