#https://leetcode.com/problems/map-sum-pairs/description/
class TrieNode():
    def __init__(self):
        self.children = {}
        self.key_value = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.keys = {}
        

    def insert(self, key: str, val: int) -> None:
        node = self.root
        if key in self.keys:
            prev_val = self.keys[key]
            self.keys[key] = val
            if prev_val == val:
                return 
            else:
                val = val - prev_val

        else:
            self.keys[key] = val

            

        for ele in key:
            if ele not in node.children:
                node.children[ele] = TrieNode()
            node = node.children[ele]
            node.key_value += val
        

    def sum(self, prefix: str) -> int:
        node = self.root
        for ele in prefix:
            if ele in node.children:
                node = node.children[ele]
            else:
                return 0
        return node.key_value



        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)



#chatpt reviews as interviewer as i came on this olution on my own  - in short it appreciated and it is the expected for faang interview
As an interviewer, I'd rate this solution **8.5/10 to 9/10**.

For a Trie-based design problem, this is actually a strong solution because you've identified the key optimization:

> Store prefix sums at each Trie node and update by the delta when a key is reinserted.

That is the optimal idea most interviewers are looking for.

---

# What you did well

### 1. Correctly handled duplicate inserts

Many candidates forget this.

Example:

```python
insert("apple", 3)
insert("apple", 5)
```

The prefix sums should increase by only `+2`, not `+5`.

You handled this via:

```python
val = val - prev_val
```

Excellent.

---

### 2. O(len(key)) Insert

```python
for ele in key:
```

Only traversing the key once.

Time:

```text
Insert = O(K)
```

where K = length of key.

Optimal.

---

### 3. O(len(prefix)) Sum

```python
return node.key_value
```

No DFS.

No subtree traversal.

No recomputation.

This is the biggest optimization.

Time:

```text
Sum = O(P)
```

where P = prefix length.

Optimal.

---

### 4. Clean Trie Design

```python
children = {}
key_value = 0
```

Very easy to understand.

---

# What would I ask in an interview?

Suppose you wrote this.

I would ask:

### Why do you need this?

```python
self.keys = {}
```

Expected answer:

> When a key is inserted again, I need its previous value to calculate the delta and update all prefix sums correctly. Without storing the previous value, I cannot know how much adjustment is required.

Good answer.

---

# Can we remove self.keys?

Short answer:

### No.

At least not while keeping O(K).

Example:

```python
insert("apple",3)
insert("apple",5)
```

Need:

```python
delta = 5 - 3
```

How do you know old value?

You must store it somewhere.

Either:

```python
self.keys[key]
```

or

store terminal value inside Trie.

````

One of these is required.

---

# Improvement #1 (Most interviewers prefer)

Instead of:

```python
self.keys = {}
````

Store value at end node.

Example:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.sum = 0
        self.value = 0
```

Then:

```python
insert("apple",5)
```

Reach last node.

```python
delta = 5 - node.value
node.value = 5
```

Then update sums.

This removes the extra hashmap.

---

### But is it actually better?

Not necessarily.

Let's compare.

| Approach            | Extra Space       |
| ------------------- | ----------------- |
| Your solution       | O(number of keys) |
| Terminal node value | O(number of keys) |

Practically the same.

Many interviewers actually prefer your version because it is simpler.

---

# Improvement #2

I would rename:

```python
key_value
```

to

```python
prefix_sum
```

Because that's what it really stores.

Current name is slightly confusing.

```python
node.prefix_sum += delta
```

is immediately understandable.

---

# Tiny Edge Case

You currently don't update root.

```python
self.root.key_value
```

always remains 0.

Not a problem because LeetCode never asks:

```python
sum("")
```

But theoretically:

```python
sum("")
```

should return total sum of all keys.

You could do:

```python
self.root.key_value += delta
```

before traversing.

Not required for the problem though.

---

# If I were evaluating communication

If you explained it like this:

> Every Trie node stores the sum of all keys passing through that prefix. On insertion, I compute the delta between new and old value and propagate only that delta along the path. Thus insert is O(K) and sum is O(P).

I'd consider that a very good explanation.

---

# Final Interview Rating

| Category           | Rating       |
| ------------------ | ------------ |
| Correctness        | 10/10        |
| Time Complexity    | 10/10        |
| Space Complexity   | 8/10         |
| Trie Understanding | 9/10         |
| Code Clarity       | 8/10         |
| Overall            | **8.5–9/10** |

For a typical LeetCode/FAANG-style interview, this is the kind of solution that would generally get a **strong hire signal for the coding round**, assuming you can clearly explain the delta-update logic and complexity analysis.


