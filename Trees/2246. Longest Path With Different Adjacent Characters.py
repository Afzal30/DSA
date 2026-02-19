class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        children = {}
        for i in range(len(parent)):
            ele = parent[i]
            if ele not in children:
                children[ele] = [i]
            else:
                children[ele].append(i)
        print(children)
        self.ans = 1
        def dfs(i):
            if i not in children:
                return 1
            
            res = 1
            for j in children[i]:
                length = dfs(j)
                if s[i] != s[j]:
                    self.ans = max(self.ans, length+res)
                    res = max(res,length+1)

            return res

        dfs(0)
        return self.ans
