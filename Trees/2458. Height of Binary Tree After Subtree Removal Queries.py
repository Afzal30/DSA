#https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        heights = {}
        def height(node):
            
            if node is None:
                return -1
            
            # compute the height of left and right subtrees
            lHeight = height(node.left)
            rHeight = height(node.right)

            h= max(lHeight, rHeight) + 1
            heights[node.val] = h
            return h

        height(root)

        ans = {}

        def dfs(node,depth,maxheight):
            if not node:
                return

            ans[node.val] = maxheight

            lefth = heights[node.left.val] if node.left else -1
            righth = heights[node.right.val] if node.right else -1

            if node.left :
                dfs(node.left,depth+1, max(maxheight,depth+1+righth))

            if node.right:
                dfs(node.right,depth+1,max(maxheight,depth+1+lefth))

        dfs(root, 0, 0)

        return [ans[q] for q in queries]
  """
  You are getting **TLE** because your algorithm recomputes the **entire tree height for every query**.

This problem is **Height of Binary Tree After Subtree Removal Queries**.

---

# Why your solution is slow

Your code:

```python
for ele in queries:
    val = height(root, ele)
```

Each call to `height()` traverses the **whole tree**.

### Complexity

If

* `n = number of nodes`
* `q = number of queries`

Then

```
height() = O(n)
Total = O(n * q)
```

Constraints in the problem:

```
n ≤ 100000
q ≤ 10000
```

Worst case:

```
100000 * 10000 = 10^9 operations
```

→ **TLE**

---

# Key Idea of the Optimal Solution

Instead of recomputing for every query, we:

1️⃣ Precompute **subtree height for every node**

2️⃣ Precompute **maximum height of the tree if that node's subtree is removed**

Then each query becomes:

```
O(1)
```

---

# Core Insight

When removing a node `X`, the remaining height depends on:

```
best path that does NOT go through X's subtree
```

So we track:

* height of each subtree
* best height available **from ancestors and siblings**

---

# Step 1: Compute subtree heights

```
height[node] = max(height[left], height[right]) + 1
```

---

# Step 2: DFS to propagate outside heights

We pass:

```
maxHeightFromParent
```

Meaning:

> Best height available **excluding current subtree**

---

# Optimal Solution

```python
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        height = {}

        # compute subtree heights
        def getHeight(node):
            if not node:
                return -1
            h = max(getHeight(node.left), getHeight(node.right)) + 1
            height[node.val] = h
            return h

        getHeight(root)

        ans = {}
        
        def dfs(node, depth, maxHeight):
            if not node:
                return

            ans[node.val] = maxHeight

            leftH = height[node.left.val] if node.left else -1
            rightH = height[node.right.val] if node.right else -1

            if node.left:
                dfs(node.left, depth + 1,
                    max(maxHeight, depth + 1 + rightH))

            if node.right:
                dfs(node.right, depth + 1,
                    max(maxHeight, depth + 1 + leftH))

        dfs(root, 0, 0)

        return [ans[q] for q in queries]
```

---

# Complexity

| Step                    | Cost |
| ----------------------- | ---- |
| Compute subtree heights | O(n) |
| DFS propagate           | O(n) |
| Queries                 | O(q) |

Total:

```
O(n + q)
```

This passes easily.

---

# Intuition Example

Tree:

```
        1
       / \
      2   3
     /
    4
```

Heights:

```
4 → 0
2 → 1
3 → 0
1 → 2
```

If we remove subtree **2**, remaining tree:

```
1
 \
  3
```

Height = **1**

We precompute this so queries become instant.

---

✅ **Rule to remember for interviews**

If a query **removes a subtree**, avoid recomputing DFS each time.
Instead compute:

```
subtree info + outside info
```

---

If you want, I can also show a **very intuitive diagram method for this problem (with leftMax/rightMax trick)** that most competitive programmers use — it makes the solution **much easier to derive in interviews.**
"""
