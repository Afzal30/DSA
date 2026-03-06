class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        tree = [ set() for _ in range(n)]

        for u,v in edges:
            tree[u].add(v)
            tree[v].add(u)

        leaf = []
        for i in range(n):
            u = i
            while len(tree[u])==1 and coins[u]==0:
                v = tree[u].pop()
                tree[v].remove(u)
                u = v

            if len(tree[u])==1:
                leaf.append(u)

        
        for size in range(2,0,-1):
            temp = []
            for u in leaf:
                if len(tree[u])==1:
                    v = tree[u].pop()
                    tree[v].remove(u)
                    if len(tree[v])==1:
                        temp.append(v)

            leaf = temp


        ans = 0
        for i in range(n):
            ans += len(tree[i])

        
        return ans


"""

This inution and approach makes the code easy to understand :

Intuition
• The goal of this code is to find the minimum number of edges that need to be removed from a given undirected tree such that the resulting graph is a forest (a collection of disjoint trees).
• To achieve this, the code first builds the tree from the given edges by creating an adjacency list representation of the graph.
• Next, the code identifies all the leaves of the tree that have zero coins. A leaf node is a node that has only one neighbor. If a node is a leaf and has zero coins, then it is removed from the tree by removing the edge that connects it to its parent node. This process is repeated until all leaf nodes with zero coins are removed from the tree.
• After removing all such nodes, the tree may still have leaves. The code then removes these leaves one by one, starting with the leaves that are farthest from the root of the tree. The code keeps track of all the leaf nodes that are removed during this process.
• Finally, the code counts the number of edges that remain in the tree after all leaf nodes with zero coins and all other leaf nodes have been removed. This count represents the minimum number of edges that need to be removed from the original tree to obtain a forest.
• The intuition behind this algorithm is to identify the nodes that are less valuable (i.e., nodes with zero coins) and remove them first. This helps in reducing the number of edges that need to be removed from the original tree to obtain a forest. After removing the less valuable nodes, the code then removes the remaining leaf nodes one by one, starting with the leaves that are farthest from the root of the tree. This helps in minimizing the number of edges that need to be removed by preserving the structure of the tree as much as possible.
Approach
Here is a step-by-step explanation of the approach used in this code:

1. Initialize the variables: The code starts by initializing the variables. The variable n represents the number of nodes in the tree (equal to the length of the coins array). The variable tree is an array of Sets, where each element represents the neighbors of a node. The variable leaf is an ArrayList that will be used to store the leaf nodes of the tree.
2. Build the tree from the edges: The input graph is represented as an array of coins and a 2D array of edges. The edges are used to build an adjacency list representation of the graph. This is done by iterating through the edges array and adding the corresponding edges to the tree array.
3. Find the leaves with zero coins: A leaf node is a node with only one neighbor. The code iterates through all nodes in the graph and checks if a node has only one neighbor and it has zero coins. If this is the case, the node is removed from the graph by removing the edge connecting it to its neighbor. This process is repeated until all leaf nodes that have zero coins are removed from the graph. The remaining leaf nodes are added to the leaf list.
4. Remove the leaves one by one: The code iteratively removes leaf nodes one by one, starting with the leaves that are farthest from the root of the tree. This is done by iterating through the leaf list and checking if a leaf node has only one neighbor. If it does, the node is removed from the graph by removing the edge connecting it to its neighbor. If the neighbor of the removed node is now a leaf node, it is added to a temporary list temp.
5. Count the remaining edges in the tree: After removing all leaf nodes, the code counts the number of edges that remain in the graph. This is done by iterating through the tree array and counting the size of each Set (i.e., the number of neighbors of each node). The sum of these sizes represents the minimum number of edges that need to be removed to disconnect the graph and make it into a forest.
Overall, the approach used in this code is to identify and remove the least valuable nodes (i.e., nodes with zero coins) first, and then iteratively remove the remaining leaf nodes while preserving the structure of the tree as much as possible. This helps in minimizing the number of edges that need to be removed to obtain a forest.
