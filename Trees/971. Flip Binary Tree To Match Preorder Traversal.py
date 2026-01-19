#https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:

        swaps = []
        i=0
        stack=[root]

        while stack:

            q = stack.pop()

            if not q.val == voyage[i]:
                return [-1]

            if q.left is None and q.right is None:
                pass
            elif q.left is None:
                if not q.right.val == voyage[i+1]:
                    return [-1]
            elif q.right is None:
                if not q.left.val == voyage[i+1]:
                    return [-1]

            else:
                if not q.left.val == voyage[i+1]:
                    q.left,q.right = q.right,q.left
                    swaps.append(q.val)

            if q.right:
                stack.append(q.right)
            if q.left:
                stack.append(q.left)

            i+=1

        return swaps
 
 
 """
 Intuition
We implement iterative pre-order of the tree. At each node during our traversal we check node's value with voyage and its children values with voyage.

If node's value disagrees: we cannot do anything and must return [-1]

if node's child value disagree: we can swap.

Note: When doing pre-order if a node has only one child, then the next value in preorder will come from existent child and therefore must not require any swap.

Complexity
Time complexity: O(n)

Space complexity: O(h)

"""
