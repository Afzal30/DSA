#https://leetcode.com/problems/task-scheduler/description/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = Counter(tasks)
        heap = [-cnt for cnt in counter.values()]
        heapq.heapify(heap)
        time = 0

        while heap:

            temp = []
            cycle = n+1

            while cycle>0 and heap:
                cnt = heapq.heappop(heap)

                if cnt +1 < 0:
                    temp.append(cnt+1)

                time +=1
                cycle-=1


            for item in temp:
                heapq.heappush(heap,item)

            if heap:
                time += cycle

        return time
"""
You’re solving Task Scheduler.
The code you posted is actually the **mathematical greedy solution**, which is **more optimal than the heap simulation**. Let's go step by step so the logic becomes very clear.

---

# 1️⃣ Problem Understanding

You have tasks like:

```
tasks = ["A","A","A","B","B","B"]
n = 2
```

Rule:

```
Same task must have at least n idle slots between them.
```

Example valid schedule:

```
A B idle A B idle A B
```

Time required:

```
8
```

---

# 2️⃣ Step-by-Step Explanation of Your Code

## Frequency counting

```python
freq = [0]*26
for task in tasks:
    freq[ord(task) - ord('A')] += 1
```

We count how many times each task appears.

Example:

```
A A A B B B
```

Frequency array:

```
A = 3
B = 3
others = 0
```

---

## Sorting frequencies

```python
freq.sort()
```

Now largest frequency is at the end.

Example:

```
[0,0,0,...,3,3]
            ↑
         freq[25]
```

---

# 3️⃣ Key Idea (Most Important Part)

Find the **task with highest frequency**.

Example:

```
A A A
```

We must separate these A's with **n cooldown slots**.

If:

```
n = 2
```

Then structure becomes:

```
A _ _ A _ _ A
```

Notice:

```
gaps between A's = freq_max - 1
```

So we create **chunks**.

---

# 4️⃣ Understanding `chunk`

```python
chunk = freq[25] - 1
```

If max frequency = 3

```
A A A
```

Then:

```
chunk = 3 - 1 = 2
```

These represent:

```
A _ _ | A _ _ | A
```

So we have **2 gaps**.

---

# 5️⃣ Idle Slots Needed

Each gap needs **n cooldown spaces**.

```python
idle = n * chunk
```

Example:

```
n = 2
chunk = 2

idle = 2 * 2 = 4
```

Structure initially:

```
A _ _ A _ _ A
```

Idle slots = 4.

---

# 6️⃣ Fill Idle Slots with Other Tasks

Now we try filling those slots with other tasks.

```python
for i in range(24,-1,-1):
    idle = idle - min(chunk,freq[i])
```

Why `min(chunk, freq[i])`?

Because each other task can fill **at most one slot per chunk**.

Example:

```
A A A
B B B
```

Structure:

```
A _ _ A _ _ A
```

Fill with B:

```
A B _ A B _ A B
```

B fills **2 gaps**.

So:

```
min(chunk, freq[B]) = min(2,3) = 2
```

Idle slots decrease.

---

# 7️⃣ Final Decision

```python
if idle > 0:
    return len(tasks) + idle
else:
    return len(tasks)
```

If idle slots remain → we must add them.

Otherwise tasks fill all spaces.

---

# Example

```
tasks = [A,A,A,B,B,B]
n = 2
```

Step-by-step:

```
max freq = 3
chunk = 2
idle = 4
```

Fill with B:

```
idle = 4 - min(2,3)
idle = 2
```

Final:

```
time = tasks + idle
= 6 + 2
= 8
```

Correct.

---

# 3️⃣ Complexity of This Solution

Time:

```
O(n)
```

Why?

* 26 fixed tasks
* Sorting 26 elements

Space:

```
O(1)
```

This is actually the **optimal solution**.

---

# Heap Simulation Solution

Interviewers often expect **this first**, then the math optimization.

### Heap Approach

```python
import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):

        counter = Counter(tasks)

        heap = [-cnt for cnt in counter.values()]
        heapq.heapify(heap)

        time = 0

        while heap:

            temp = []
            cycle = n + 1

            while cycle > 0 and heap:

                cnt = heapq.heappop(heap)
                if cnt + 1 < 0:
                    temp.append(cnt + 1)

                time += 1
                cycle -= 1

            for item in temp:
                heapq.heappush(heap, item)

            if heap:
                time += cycle

        return time
```

---

# Heap Solution Intuition

Always schedule **most frequent task first**.

Example:

```
A A A B B B
```

Max heap:

```
A(3), B(3)
```

Cycle size:

```
n + 1
```

So we run:

```
A B idle
A B idle
A B
```

---

# Complexity of Heap Solution

Let:

```
t = number of tasks
```

Time:

```
O(t log 26)
```

Since heap size ≤ 26.

Simplified:

```
O(t)
```

Space:

```
O(26)
```

---

# Interview Insight

For this problem, best progression is:

1️⃣ Heap simulation solution
2️⃣ Mathematical greedy optimization

Your current solution is **already the optimal one**, which is excellent.

---

✅ Since you’ve now solved:

* K Closest Points to Origin
* Top K Frequent Elements
* Find K Pairs with Smallest Sums
* Task Scheduler

you’ve basically covered **most heap interview patterns**.

If you'd like, I can also show you the **2 hardest heap interview problems that companies like Google/Meta love asking**, which will fully complete your heap mastery.
"""
