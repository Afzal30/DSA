#https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/
MOD = 1_000_000_007
class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
         # Step 1: Build the tree (parent -> children)
        tree = defaultdict(list)
        for child, parent in enumerate(prevRoom):
            tree[parent].append(child)

        # Step 2: DFS returns:
        # (number_of_ways_to_build_subtree, subtree_size)
        def dfs(node: int) -> tuple[int, int]:
            # Leaf node
            if not tree[node]:
                return 1, 1  # 1 way, size = 1

            total_ways = 1
            total_nodes = 0  # nodes processed so far from children

            for child in tree[node]:
                child_ways, child_size = dfs(child)

                # Multiply child internal arrangements
                total_ways = (total_ways * child_ways) % MOD

                # Count ways to interleave current child subtree
                # with previously processed children
                total_ways = (
                    total_ways * math.comb(total_nodes + child_size, child_size)
                ) % MOD

                # Update processed nodes
                total_nodes += child_size

            # Include current node itself
            return total_ways, total_nodes + 1

        # Root is always room 0
        return dfs(0)[0]


"""
Nice choice of solution — this is a **classic DFS + combinatorics** pattern, and once it clicks, this problem feels *beautiful* rather than scary 😄
Let’s go **line by line**, but more importantly, I’ll explain **what each variable *means*** and **why the math is correct**.

---

## 🔁 Big Picture (before code)

* `prevRoom` defines a **tree**
* Rule: **parent must be built before child**
* Goal: count **valid build orders**
* This is equivalent to counting **topological orderings of a tree**
* Strategy:

  * Build the tree
  * DFS from root
  * For each node:

    * Count ways to build its subtrees
    * Count ways to **interleave** those subtrees

---

## 🧱 Step 1: Build the tree

```python
g = collections.defaultdict(list)
for cur, pre in enumerate(prevRoom):
    g[pre].append(cur)
```

### What’s happening?

* `g[parent] = [children...]`
* We reverse the `prevRoom` array to adjacency list

Example:

```python
prevRoom = [-1, 0, 0, 1, 2]
```

Tree becomes:

```
        0
      /   \
     1     2
    /       \
   3         4
```

So:

```python
g[-1] = [0]
g[0]  = [1, 2]
g[1]  = [3]
g[2]  = [4]
```

We start DFS from node `0`.

---

## 🔁 Step 2: DFS function contract (VERY IMPORTANT)

```python
def dfs(cur):
    return (ways, size)
```

### Meaning:

* `ways` → number of valid build orders **inside this subtree**
* `size` → total number of nodes in this subtree (including `cur`)

This pair is the heart of the solution.

---

## 🍃 Base Case: Leaf node

```python
if not g[cur]:
    return 1, 1
```

### Why?

* A leaf has:

  * Exactly **1 way** to build (just itself)
  * Subtree size = 1

✅ Makes perfect sense.

---

## 🧠 Core Logic (Most Important Part)

```python
ans, l = 1, 0
```

### Meaning:

* `ans` → total ways for `cur`’s subtree
* `l` → total nodes processed so far from children

Think of `l` as:

> “How many nodes have I already placed from previous child subtrees?”

---

## 🔄 Process each child

```python
for nxt in g[cur]:
    tmp, r = dfs(nxt)
```

* `tmp` → ways to build `nxt`’s subtree
* `r` → size of `nxt`’s subtree

---

## 🧩 The Key Formula (Interleaving Logic)

```python
ans = (ans * tmp * math.comb(l + r, r)) % MOD
```

This line deserves a **slow, deep explanation**.

---

### 🟦 Why multiply by `tmp`?

Each child subtree has its **own internal build orders**.
Those are independent choices.

So:

```
total ways *= child ways
```

---

### 🟨 Why `math.comb(l + r, r)`?

This counts **how many ways we can interleave**:

* `l` = nodes from previous children
* `r` = nodes from current child
* Total positions = `l + r`
* Choose positions for the `r` nodes

[
\text{ways to interleave} = \binom{l+r}{r}
]

This ensures:

* Internal order of each subtree is preserved
* Relative order across subtrees is flexible

📌 This is the **combinatorics backbone** of the solution.

---

### 🔁 Then update total size

```python
l += r
```

Now future children must interleave with **all previous nodes**.

---

## 🔚 After processing all children

```python
return ans, l + 1
```

* `l` = total nodes from children
* `+1` → include current node

So:

* subtree size = children + self

---

## 🏁 Final Answer

```python
return dfs(0)[0]
```

Start from root:

* Take only the **number of ways**
* Ignore size at the top level

---

## 🧠 Intuition Summary (Mental Model)

* Each subtree is a **block of tasks**
* Parent must come before children
* Children subtrees can be **woven together**
* DFS builds answers bottom-up
* `math.comb` counts **valid weaving patterns**

---

## ⏱ Complexity

* Time: **O(n)** (DFS + constant-time combinatorics)
* Space: **O(n)** (tree + recursion)

---

## 🔥 Final Thought

This problem is a **perfect blend** of:

* Tree DFS
* Topological ordering intuition
* Combinatorics (multinomial coefficient)

Once you understand **what `l`, `r`, and `comb(l+r, r)` represent**, the solution becomes *inevitable*.

If you want:

* a **dry run on a concrete input**
* or a **visual explanation**
* or a **rewrite with comments for revision**

Just say the word 👌
"""


"""
Idea

We can view the ant colony as a tree. Why tree but not general graph? Because each room can only have one prevRoom. Recursion is our friend in solving tree problems.

Define dfs(cur) as the number of ways to build rooms if we start at node cur. The base case is simply dfs(leaf) = 1, but the recursive step is kind of tricky.

Here are my thoughts when approach this problem:

First think of a simple scenairo where a node has two branches and each branch is a chain (dfs(child) = 1). What is dfs(cur)? This is equivalent to count the number of ways to combine two arrays and maintain their original order. Say the lengths of these two arrays are l and r, the answer is math.comb(l+r, l). Another way of thinking this is to put l items into l+r spots and fill the remaining spots with the other r items.

Next, what if the branch is not a chain? Say dfs(left_child)=x and dfs(right_child)=y. We just multiply them together. So the solution becomes x * y * math.comb(l+r, l).

Finally, what if there are many branches? We can combine them one by one: take the leftmost two branches first, get the merged branch, merge it with the third branch, and so on.

Please see code below fore more details =)

Edit: Calculate n chooses k without math.comb

For Python users, math.comb comes in handy. But what if you have to calculate math.comb(n, k) without using the built-in function? One may think of caching fac(n) and calculating it as comb(n, k) = n! / (k! * (n-k)!). But this is not enough - we have to incorporate mod into this whole equation.

To solve this issue, we can use Modular Multiplicative Inverse as a workaround. It's very hard to implement this without knowing the method beforehand and I think it's unfair for non-Python users to implement this during the content. I added a workable C++ solution to this post for reference.

Disclaimer: I did not implement the C++ solution by myself. The solution is borrowed from the top voted solutions in leetcode-cn solution section. If you could please go upvote those solutions instead.


Python

class Solution:
    def waysToBuildRooms(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        g = collections.defaultdict(list)
        for cur, pre in enumerate(arr):
            g[pre].append(cur)
            
        def dfs(cur):
            if not g[cur]:
                return 1, 1
            ans, l = 1, 0
            for nxt in g[cur]:
                tmp, r = dfs(nxt)
                ans = (ans * tmp * math.comb(l+r, r)) % MOD
                l += r
            return ans, l + 1
            
        return dfs(0)[0]
"""
