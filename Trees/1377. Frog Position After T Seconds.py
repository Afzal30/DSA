#1377. Frog Position After T Seconds
#https://leetcode.com/problems/frog-position-after-t-seconds/description/

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        graph = defaultdict(set)

        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)

        q = deque([(1,1.0,0)])   # node, probability, time
        visited = set([1])

        while q:
            node, prob, time = q.popleft()

            if time == t:
                if node == target:
                    return prob
                continue

            children = [nei for nei in graph[node] if nei not in visited]

            if not children:
                if node == target:
                    return prob
                continue

            p = prob / len(children)

            for nei in children:
                visited.add(nei)
                q.append((nei,p,time+1))

        return 0

"""
The problem **Frog Position After T Seconds** is a **tree probability + BFS/DFS simulation** problem.

I'll explain the **intuitive idea with a diagram and step-by-step reasoning**, which usually makes it much easier to implement.

---

# 🐸 Problem Intuition

You have:

* `n` nodes forming a **tree**
* Frog starts at **node 1**
* Every second:

  * Frog jumps to **one unvisited neighbor**
  * Each neighbor has **equal probability**
* If a node has **no unvisited neighbors**, frog **stays there**

You must compute:

```
Probability frog is at target after t seconds
```

---

# 🌳 Example Tree

Example:

```
n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 2
target = 4
```

Tree:

```
        1
      / | \
     2  3  7
    / \   \
   4   6   5
```

---

# ⏱ Step 0

Start:

```
time = 0
frog at 1
probability = 1
```

---

# ⏱ Step 1

Node `1` has **3 neighbors**

```
2,3,7
```

So probability splits:

```
P(2) = 1/3
P(3) = 1/3
P(7) = 1/3
```

Diagram:

```
        1
      / | \
   1/3 1/3 1/3
    2   3   7
```

---

# ⏱ Step 2

Now frog moves again.

### From node 2

Unvisited neighbors:

```
4,6
```

Split:

```
P(4) = (1/3)*(1/2) = 1/6
P(6) = (1/3)*(1/2) = 1/6
```

---

### From node 3

Unvisited neighbor:

```
5
```

```
P(5) = 1/3
```

---

### From node 7

Leaf node → stays

```
P(7) = 1/3
```

---

# Final State at t = 2

```
node : probability

4 → 1/6
6 → 1/6
5 → 1/3
7 → 1/3
```

If:

```
target = 4
```

Answer:

```
1/6
```

---

# 🧠 Key Rules

### 1️⃣ Never go to visited nodes

This prevents moving back to parent.

---

### 2️⃣ If leaf before t seconds

Frog **stays there**.

Example:

```
1 - 2
```

t = 3

```
1 → 2 → stay → stay
```

---

### 3️⃣ If target reached but it still has children

The frog **must move away**, so probability becomes **0**.

Example:

```
1 → 2 → 3
```

If:

```
target = 2
t = 2
```

Frog moves to 3 → cannot stay at 2.

---

# 🚀 Clean BFS Solution

```python
from collections import defaultdict, deque

class Solution:
    def frogPosition(self, n, edges, t, target):

        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([(1,1.0,0)])   # node, probability, time
        visited = set([1])

        while q:
            node, prob, time = q.popleft()

            if time == t:
                if node == target:
                    return prob
                continue

            children = [nei for nei in graph[node] if nei not in visited]

            if not children:
                if node == target:
                    return prob
                continue

            p = prob / len(children)

            for nei in children:
                visited.add(nei)
                q.append((nei,p,time+1))

        return 0
```

---

# ⏱ Complexity

```
Time  : O(n)
Space : O(n)
```

Each node visited once.

---

# 🎯 Trick Interviewers Expect

The **two tricky cases**:

1️⃣ Reaching target **early but has children → probability becomes 0**

2️⃣ Reaching **leaf early → frog stays**

---

✅ If you'd like, I can also show the **one-line mathematical DFS trick** many competitive programmers use for this problem (even cleaner than BFS).
"""
