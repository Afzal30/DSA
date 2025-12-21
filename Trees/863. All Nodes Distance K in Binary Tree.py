#https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        
        def buildgraph(node,parent,graph):
            if not node:
                return
            
            if node not in graph:
                graph[node] = []

            if parent:
                graph[node].append(parent)
                graph[parent].append(node)

            buildgraph(node.left,node,graph)
            buildgraph(node.right,node,graph)



        mydict={}
        buildgraph(root,None,mydict)

        queue =[ (target,0) ]
        visited = set([target])
        result = []

        while queue:
            node,distance = queue.pop(0)

            if distance == k:
                result.append(node.val)

            if distance>k :
                break

            for neighbour in mydict[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour,distance+1))

        return result

        
