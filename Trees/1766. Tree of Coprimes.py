#https://leetcode.com/problems/tree-of-coprimes/
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        ans = [-1]*len(nums)
        path = [ [] for _ in range(51)]
        seen = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)


        def dfs(node, depth):
            if node in seen:
                return
            #print("node , nums[node]",node, nums[node])
            seen.add(node)
            largestdepth = -1

            for x in range(1,51):
                if gcd(nums[node],x) == 1:
                    #print("x",x)
                    if len( path[x])>0:
                        #print("path[x]",path[x])
                        topnode, topdepth = path[x][-1]
                        #print("topnode, topdepth" , topnode, topdepth)
                        if largestdepth < topdepth:
                            largestdepth = topdepth
                            ans[node] = topnode

                        #print("largestdepth", largestdepth)
                        #print("ans[node]",ans[node])


            path[ nums[node] ].append((node,depth))
            #print("path",path[ nums[node] ])
            for nei in graph[node]:
                dfs(nei,depth+1)
            #print("path before pop",path[ nums[node] ])
            path[nums[node]].pop()
            #print("path pop",path[ nums[node] ])


        dfs(0,0)
        return ans
"""

idea:
Please notice in the constraints that all node values is in range 1..50.
We create an array of 51 elements path[51] where path[x] contains list of nodes from root to current node which their node's value are equal to x.
While traversing nodes using DFS, for current node we can check all paths path[x] (up to 50) where x and current node are co-prime then we try to pick the node which is close to current node as our ancestor.
A node is close to current node if its depth is largest.


Nice — this is actually a **very good evolution** of your earlier attempt 👍
What you’ve written is a **correct DFS + path-state solution**, very close to the optimal editorial approach. I’ll explain **exactly what each part does**, *why it works*, and *what to slightly improve*.

---

## 1️⃣ High-level idea (what your code is doing)

For every node in the tree, you want:

> the **closest ancestor** whose value is **coprime** with the current node’s value.

Your strategy:

* DFS from root
* Maintain a **path state** (`path[value]`)
* For each node:

  * Look at all values `1..50`
  * If coprime and present on path → candidate ancestor
  * Pick the **deepest** one (closest)

This is **exactly the right approach**.

---

## 2️⃣ Data structures (why each exists)

### `graph`

```python
graph = defaultdict(list)
```

Undirected adjacency list for the tree.

---

### `ans`

```python
ans = [-1]*len(nums)
```

Final answer array:

```text
ans[i] = closest coprime ancestor of node i
```

---

### `path`

```python
path = [[] for _ in range(51)]
```

This is the **most important structure**.

Meaning:

```text
path[x] = stack of (node, depth)
```

* Contains **only ancestors** of the current DFS node
* Maintained via push before DFS → pop after DFS
* Stack top = **nearest ancestor with value x**

Example:

```text
DFS path: 0 → 3 → 7
values:     2   6   9

path[2] = [(0,0)]
path[6] = [(3,1)]
path[9] = [(7,2)]
```

---

### `seen`

```python
seen = set()
```

Used to:

* Prevent revisiting parent nodes
* Avoid infinite loops (tree is undirected)

---

## 3️⃣ DFS function: step-by-step

### Function signature

```python
def dfs(node, depth):
```

* `node` → current node
* `depth` → depth in DFS tree

---

### 3.1 Stop revisits

```python
if node in seen:
    return
seen.add(node)
```

Ensures each node is processed **once**.

---

### 3.2 Find closest coprime ancestor

```python
largestdepth = -1
```

Tracks **deepest valid ancestor**.

---

### Loop over all values (1..50)

```python
for x in range(1,51):
```

Why this works:

* `nums[i] ≤ 50`
* Instead of walking ancestors, you check **values**

---

### Coprime check

```python
if gcd(nums[node], x) == 1:
```

If value `x` is coprime with current node.

---

### Check if such ancestor exists

```python
if len(path[x]) > 0:
```

If true:

* There exists an ancestor with value `x`

---

### Extract nearest ancestor

```python
topnode, topdepth = path[x][-1]
```

Because:

* Stack top = closest ancestor with value `x`

---

### Choose nearest one

```python
if largestdepth < topdepth:
    largestdepth = topdepth
    ans[node] = topnode
```

This guarantees:

> **Closest ancestor wins**

---

### Result after loop

```python
ans[node] = closest coprime ancestor or -1
```

---

## 4️⃣ Add current node to path

```python
path[nums[node]].append((node, depth))
```

This means:

> “From now on, this node is an ancestor for deeper nodes”

---

## 5️⃣ DFS into children

```python
for nei in graph[node]:
    dfs(nei, depth+1)
```

Traverse tree normally.

---

## 6️⃣ Backtracking (critical)

```python
path[nums[node]].pop()
```

This removes the node **after returning**.

Why this is mandatory:

* Ensures sibling branches do not see this node
* Keeps `path` accurate for each DFS path

🚨 Without this → WRONG ANSWERS.

---

## 7️⃣ DFS entry point

```python
dfs(0,0)
```

Root is node `0` (problem guarantees tree rooted at 0).

---

## 8️⃣ Time & space complexity

### Time

```text
DFS nodes: N
For each node: 50 gcd checks
→ O(N × 50)
```

### Space

```text
path: 51 stacks
graph: N
```

Efficient and optimal ✔

---

## 9️⃣ Why this solution is GOOD (important)

Compared to your **first solution**:

| Old version       | Current version     |
| ----------------- | ------------------- |
| Walk parent chain | Value-based lookup  |
| O(N²)             | O(N × 50)           |
| Parent confusion  | DFS rooted tree     |
| No path state     | Proper backtracking |

This is **interview-ready logic**.

---

## 🔧 Small improvements (optional but clean)

### Replace `seen` with parent argument

```python
def dfs(node, parent, depth):
    ...
    for nei in graph[node]:
        if nei != parent:
            dfs(nei, node, depth+1)
```

Cleaner and faster.

---

### Remove debug prints before submission

You already know this 😉

---

## 🎯 Final assessment (based on THIS code)

🔥 You now demonstrate:

* Tree DFS mastery
* Path-state reasoning
* Constraint-driven optimization
* Correct backtracking

👉 **This is solid SDE-1 / early SDE-2 level tree handling.**

---

## Want next?

I can:

* Dry-run this code on your big failing test
* Convert it into the editorial version
* Show how interviewers expect you to explain this

Just say the word 👊
"""
