#https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/description/

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        g = defaultdict(set)
        for u,v in  pairs:
            g[u].add(v)
            g[v].add(u)

        #print("G", g)

        def helper(nodes):
            #print("nodes",nodes)
            d = defaultdict(list)
            m = len(nodes)-1
            #print("m",m)

            for node in nodes:
                #print(" g[node] ,len(g[node])",g[node] , len(g[node]))
                d[len(g[node])].append(node)

            #print("D", d)

            if len(d[m])==0:
                return 0


            root = d[m][0]

            for node in g[root]:
                g[node].remove(root)

            comps = defaultdict(set)
            seen = set()
            i = 0

            def dfs(node,i):
                comps[i].add(node)
                seen.add(node)
                for neighb in g[node]:
                    if neighb not in seen:
                        dfs(neighb,i)

            for node in nodes:
                if node != root and node not in seen:
                    dfs(node,i)
                    i+=1

            #print("comps",comps)
            #print("seen",seen)

            cands = [ helper(comps[ele]) for ele in comps]
            #print("cands",cands)

            if 0 in cands  : return 0
            if 2 in cands  : return 2
            if len(d[m])>=2: return 2

            
            return 1


        
        return helper(set(g.keys()))


"""
Nice, this is a **really good question** — this exact part is where most people feel the solution “works by magic”. Let’s de-mystify it carefully.

I’ll **not re-explain the whole problem**, only the part you’re stuck on.

---

## First: what does `helper(nodes)` RETURN mean?

This is **critical**.
`helper(nodes)` can return **only 3 values**:

| Return | Meaning                            |
| ------ | ---------------------------------- |
| `0`    | ❌ Impossible to build a valid tree |
| `1`    | ✅ Exactly **one** valid tree       |
| `2`    | ✅ **Multiple** valid trees         |

So `helper` is not building the tree —
it’s answering: **how many ways can this subtree be formed?**

---

## What is `comps` at this point?

Earlier, you did:

```python
root = d[m][0]
for node in g[root]:
    g[node].remove(root)
```

This **removes the root**, which splits the graph into **connected components**.

```python
comps = {
    0: {nodes of component 0},
    1: {nodes of component 1},
    ...
}
```

Each component must become **one child subtree of `root`**.

---

## Now this line 👇

```python
cands = [helper(comps[ele]) for ele in comps]
```

### What this actually means

For **each child subtree**, recursively compute:

> Is that subtree impossible / unique / multiple?

So `cands` is something like:

```python
cands = [1, 1, 2]
```

Meaning:

* subtree 1 → unique
* subtree 2 → unique
* subtree 3 → multiple ways

---

## Why the next checks make sense

Let’s go line by line.

---

### 1️⃣ If **any subtree is impossible**

```python
if 0 in cands:
    return 0
```

Why?

If even **one child subtree cannot form a valid tree**,
then the whole tree is impossible.

👉 One broken part breaks the entire structure.

---

### 2️⃣ If **any subtree has multiple ways**

```python
if 2 in cands:
    return 2
```

Why?

If **one child subtree** can be arranged in multiple ways,
then the **entire tree** also has multiple ways.

Even if everything else is fixed, this part isn’t.

---

### 3️⃣ If the root itself is ambiguous

```python
if len(d[m]) >= 2:
    return 2
```

Recall:

```python
d[m] = nodes whose degree == m
```

That means:

* These nodes connect to **all other nodes**
* Any of them could be the root

So:

* 2+ valid root choices → multiple valid trees

---

### 4️⃣ Otherwise

```python
return 1
```

Means:

* Every subtree is uniquely determined
* Root choice is unique
* So the entire tree is unique

---

## Tiny example to lock this in

Suppose after splitting:

```python
comps = {
    0: {2,3},
    1: {4}
}
```

And recursion returns:

```python
cands = [1, 2]
```

Meaning:

* subtree `{2,3}` → unique
* subtree `{4}` → multiple

Result?

```python
if 2 in cands: return 2
```

✔ Correct — whole tree has multiple constructions.

---

## Big picture (mental model)

Think of `helper` like this:

> “Given these nodes, how many valid trees can I form?”

And `cands` answers:

> “How many ways can **each child subtree** be formed?”

Then we combine results with simple logic:

* Any `0` → whole thing collapses
* Any `2` → ambiguity spreads upward
* Multiple root choices → ambiguity
* Else → exactly one way

---

## One-sentence intuition (important)

> Tree ambiguity **propagates upward** — if any subtree or root choice is ambiguous, the entire structure becomes ambiguous.

---

If you want next, I can:

* Walk through a **concrete input** step-by-step
* Draw a **recursion tree**
* Or explain **why degree = n−1 ⇒ root**

Just tell me 👍
"""
