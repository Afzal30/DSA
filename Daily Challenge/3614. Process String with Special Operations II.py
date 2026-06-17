class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0

        # Step 1: compute final length
        for c in s:
            if c == '*':
                length = max(0, length - 1)
            elif c == '#':
                length *= 2
            elif c != '%':
                length += 1

        if k >= length:
            return '.'

        # Step 2: backward simulation
        for i in range(len(s) - 1, -1, -1):
            c = s[i]

            if c == '*':
                length += 1

            elif c == '#':
                half = length // 2
                if k >= half:
                    k -= half
                length = half

            elif c == '%':
                k = length - 1 - k

            else:
                if k == length - 1:
                    return c
                length -= 1

        return '.'



"""
Idea
We are given a string with special operations, and instead of actually building the final string (which can grow very large), we track only how the string would behave.

Here’s the key observation:

👉 We only care about the final character at index k, not the full string.

So we break the problem into two phases:

First, compute the final length after all operations.
Then, walk backward and figure out where index k comes from.
This turns a potentially expensive simulation into a linear one.

Approach
Step 1: Forward Pass — Compute Final Length
We simulate how the string length changes:

Normal character (a-z)

adds one character → len++
'*'

deletes last character (if exists)
→ len = max(0, len - 1)
'#'

duplicates string
→ len *= 2
'%'

no change in length
Why this works?
We don’t need actual string content yet — only how big it becomes.

Think of it like tracking “capacity growth” instead of building the container.

Step 2: Boundary Check
After forward pass:

if k >= len → return '.'
Because index k does not exist in final string.

Step 3: Backward Pass — Reverse Simulation
Now we move from right to left and undo operations.

We maintain:

len = current simulated length
k = target index we are tracking backward
Case 1: Normal Character
If current character is not special:

It contributes one position at the end of current string.
So:
if k == len - 1 → return character
else len--
👉 We are basically saying:
“If this was the last character in this version, we found our answer.”

Case 2: '*' (Deletion)
Forward: removes last character
Backward: restores length

len++
👉 We are undoing the deletion.

Case 3: '#' (Doubling)
Forward:

S → S + S
Backward:
We map index back to original half:

half = len / 2
If k >= half → it came from second half:

k -= half
Then:

len /= 2
Case 4: '%' (Reverse)
Forward:

reverse string
Backward:
We reverse index mapping:

k = len - 1 - k
👉 This flips position inside current length.

"""
