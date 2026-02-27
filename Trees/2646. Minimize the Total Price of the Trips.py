#https://leetcode.com/problems/minimize-the-total-price-of-the-trips/description/

class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:

        def bfs(src,dst):
            q = [ (src,[src])]
            visited = set()
            

            while q:
                node,path = q.pop(0)

                if node == dst:
                    return path

                visited.add(node)

                for neigh in graph[node]:
                    if neigh not in visited:
                        q.append((neigh,path+[neigh]))

                    


        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        freq = defaultdict(int)
        for src,dst in trips:
            path = bfs(src,dst)
            for node in path:
                freq[node]+=1

        print(freq)

        def dp(node,parent,can_half):
            if (node,parent,can_half) in memo:
                return memo[(node,parent,can_half) ]
            if can_half:
                cost = freq[node] * (price[node]//2)
            else:
                cost = freq[node] * price[node]

            for nei in graph[node]:
                if nei != parent:
                    if can_half:
                        nei_cost = dp(nei,node,False)
                    else:
                        nei_cost = min( dp(nei,node,True) , dp(nei,node,False))

                    cost += nei_cost

            memo[(node,parent,can_half) ] = cost
            return cost

        tot_cost = math.inf
        memo = {}
        for node in range(n):
            tot_cost = min(tot_cost,dp(node,None,True) , dp(node,None,False))

        return tot_cost


#https://www.youtube.com/watch?v=VI-X7AbMFxg





        
