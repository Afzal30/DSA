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
"""Quite painful problem, to be honest. Not a lot of people managed to solve it during contest.

First idea we need to understand, is that A pair [xi, yi] exists in pairs if and only if xi is an ancestor of yi or yi is an ancestor of xi. Let us illustrate this on example of tree:

5
| \
4 3
| \
1 2

We will have pairs [1, 4], [1, 5], [2,4], [2,5], [3,5], [4,5], that is all pairs with two nodes, on which is ancestor of another. What we can notice, if it is possible to create such a tree, that one node will be ancestor of all other nodes, that is in case, there will be pairs [1, 5], [2, 5], [3, 5], [4, 5].

Now, let us go to the algorithm:

First, create graph from our pairs array.
Function helper(nodes) have input set of nodes and try to solve subproblem with this set.
We discussed, that we need to find node which is connected with all other nodes, that is its degree should be equal to m = len(nodes) - 1.
If we did not found such a node, we can immedietly return 0: it is not possible to recunstruct a tree.
If there is such a node, let us denote it root. Actually, it can happen that there is more than one node with this property and in this case any of them can be root and if we have say U possible solution with first of them being root, that there will be exactly U possible solutions if another will be root - we can just replace one of them with another.
Now, we clean our graph g: we remove all connections between root and all its neighbours (actually it is enough to cut only one way connections)
Next step is to perform dfs to find connected components.
Finally, we run our helper function on each of found components: if it happens that for some subproblem we have answer 0, it means that for original problem we also need to return 0. If 0 not here and we met 2 in our cands, than we return 2: it means, that we found 2 or more solutions for some subproblems and 1 for others, like cands = [1, 2, 1, 1, 2]. In this case, we can be sure, that we have more than 2 solutions (in fact we have 1*2*1*1*2). Finally, important point: if we have len(d[m]) >= 2, we also return 2 - see step 5.
Complexity: this is the most interesting part. Imagine, that we have n nodes in our graph. Then on each step we split our data into several parts and run helper function recursively on each part, such that sum of sizes is equal to n-1 on the first step and so on. So, each element in helper(nodes) can be used no more than n times, and we can estimate it as O(n^2). Also, we need to consider for node in g[root]: g[node].remove(root) line, which for each run of helper can be estimated as O(E), where E is total number of edges in g. Finally, there is part, where we look for connected components, which can be estimated as O(E*n), because we will have no more than n levels of recursion and on each level we use each edge no more than 1 time. So, final time complexity is O(E*n). I think, this estimate can be improved to O(n^2), but I do not know at the moment, how to do it. Space complexity is O(n^2) to keep all stack of recursion.
"""

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
