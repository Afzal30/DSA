#https://leetcode.com/problems/validate-binary-tree-nodes/
from queue import Queue
class Solution:
    def isBinaryTreeValid(self, root: int, leftChild: List[int], rightChild: List[int]) -> bool:
        visited = [False] * len(leftChild)  # Tracks visited nodes
        nodeQueue = Queue()  # Queue for BFS traversal
        nodeQueue.put(root)
        visited[root] = True

        while not nodeQueue.empty():
            current = nodeQueue.get()

            # Check left child
            if leftChild[current] != -1:
                if visited[leftChild[current]]:  # Check for cycle
                    return False

                nodeQueue.put(leftChild[current])
                visited[leftChild[current]] = True  # Mark left child as visited

            # Check right child
            if rightChild[current] != -1:
                if visited[rightChild[current]]:  # Check for cycle
                    return False

                nodeQueue.put(rightChild[current])
                visited[rightChild[current]] = True  # Mark right child as visited

        # Check if there are multiple components
        for visit in visited:
            if not visit:
                return False

        return True  # All nodes form a valid binary tree

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        childCount = [False] * n  # Tracks child count for each node

        #First logic:  a node can be either left chile of someother node or right child of some other node (except root), so if a node is present in left child and in right child list, it is not a valid binary tree

        # Update child count based on leftChild
        for child in leftChild:
            # Check if node has child
            if child != -1:
                childCount[child] = True  # Mark left child as having a parent

        # Update child count based on rightChild
        for child in rightChild:
            # Check if node has child
            if child != -1:
                if childCount[child]:  # Check if the right child already has a parent
                    return False

                childCount[child] = True  # Mark right child as having a parent


#Second logic, even though node is only either present in left or right not in both, it is possible that more than one root node present in the tree
        root = -1  # Root node
        for i in range(n):
            if not childCount[i]:
                if root == -1:
                    root = i  # Set root node if not assigned
                else:
                    return False  # Multiple roots found, not a valid binary tree

#Third : we are unable to find the root node, not a valid binary tree
        if root == -1:
            return False  # No root found, not a valid binary tree
        
        #if all the above three condition satisfies, we still need to check 
        #Foruth : Check for cycle
        #Fifth :  Check if there are multiple components

        return self.isBinaryTreeValid(root, leftChild, rightChild)  # Check if the tree is valid
