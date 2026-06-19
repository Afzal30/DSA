#648. Replace Words

class TrieNode():
    def __init__(self):
        self.children = {}
        self.isend = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for ele in word:
            if ele not in node.children:
                node.children[ele] = TrieNode()
            node = node.children[ele]

        node.isend = True

    def search_root(self,word):
        node = self.root
        root_word = ""
        for ele in word:
            if ele not in node.children:
                break
            node = node.children[ele]
            root_word +=ele
            if node.isend:
                return root_word

        if node.isend:
            return root_word
        else:
            return word

            



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        trie = Trie()

        for ele in dictionary:
            trie.insert(ele)

        sen_words = sentence.split()

        res = []

        for ele in sen_words:
            res.append(trie.search_root(ele))

        return " ".join(res)


#solved on own

"""
This version is **clean, correct, and interview-ready**. Compared to your earlier one, this is a clear improvement.

Let me evaluate it the way an interviewer would.

---

# ⭐ Final Interview Rating: 8.5 / 10

This is a **strong Trie implementation** for Replace Words.

You are comfortably in “good hire” territory for coding, with a few polish gaps for “strong hire”.

---

# ✅ What You Did Really Well

## 1. Correct Trie Design

```python
self.children = {}
self.isend = False
```

This is the standard clean Trie structure.

No unnecessary complexity. Good.

---

## 2. Correct Problem Mapping

You correctly identified:

> We should stop at the shortest root → Trie with early termination.

This is the key insight.

---

## 3. Early Exit Optimization (Very Important)

```python
if node.isend:
    return root_word
```

This is exactly what makes the solution optimal.

You are not searching full word unnecessarily.

---

## 4. Proper Sentence Handling

```python
sen_words = sentence.split()
```

Clean separation of concerns.

Good readability.

---

## 5. Correct Output Construction

```python
res = []
return " ".join(res)
```

This is **Python best practice**.

Avoids O(N²) string concatenation problem.

This is a **strong signal to interviewers** that you understand Python internals.

---

# ⚠️ Areas for Improvement (Important Interview Feedback)

## 1. Minor Inefficiency: `root_word += ele`

```python
root_word += ele
```

This is still **O(k²)** in worst case inside search.

Why?

Because strings are immutable.

Even though overall complexity is fine due to small constraints, interviewers may point it out.

### Better approach:

Instead of building string step-by-step:

You can track index:

```python
def search_root(self, word):
    node = self.root
    for i, ch in enumerate(word):
        if ch not in node.children:
            break
        node = node.children[ch]
        if node.isend:
            return word[:i+1]
    return word
```

### Why better:

* No repeated string concatenation
* Cleaner and more optimal

---

## 2. Edge Case Clarity

This block:

```python
if node.isend:
    return root_word
else:
    return word
```

Works, but is slightly redundant.

You already handle return inside loop.

You could simplify logic flow.

---

## 3. Missing Type Safety / Clean API Design

Not a big issue, but in interviews:

You could optionally add:

```python
def insert(self, word: str) -> None:
```

Makes code more production-ready.

---

## 4. No Need for `print` (you fixed this 👍)

Good that it's removed in final version.

---

# 🧠 What Interviewers Are Testing Here

They are not just testing Trie.

They are testing:

### 1. Prefix search understanding

You nailed this.

### 2. Early termination logic

You nailed this.

### 3. Python performance awareness

You improved this with `.join()` → strong signal.

### 4. Code cleanliness

Mostly good, minor string concat issue remains.

---

# 🔥 What Would Push This to 9.5/10

If you changed just ONE thing:

### Replace this:

```python
root_word += ele
```

### With this:

```python
return word[:i+1]
```

That’s it.

This removes:

* unnecessary string building
* improves clarity
* shows deeper optimization thinking

---

# 🧾 Final Verdict

| Category               | Score    |
| ---------------------- | -------- |
| Correctness            | 10/10    |
| Trie Usage             | 9/10     |
| Time Complexity        | 8.5/10   |
| Pythonic Code          | 8.5/10   |
| Optimization Awareness | 8/10     |
| Overall                | ⭐ 8.5/10 |

---

# 💬 Honest Interview Summary

If I were interviewing you:

* I would say: **"Strong candidate"**
* I would likely give: **Hire / Strong Hire (depending on system design round)**
* Main feedback would be:

  * avoid string concatenation in loops
  * simplify search logic using slicing/index

---

If you want, I can show you:

* 🔥 3 alternate solutions (HashSet, BFS Trie, DFS Trie)
* 💡 or how to convert this into a “Google-level follow-up question” (they often extend this problem)
"""

    
