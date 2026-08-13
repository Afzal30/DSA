class Solution:
    def longestRepeating(self, s: str, queryCharacters: str,
                         queryIndices: List[int]) -> List[int]:

        n = len(s)
        tree = [None] * (4 * n)
        s = list(s)

        def merge(a, b):
            if not a:
                return b
            if not b:
                return a

            length = a[0] + b[0]
            pref = a[1]
            suff = b[2]
            best = max(a[3], b[3])

            if a[4] == b[4]:
                best = max(best, a[2] + b[1])

                if a[1] == a[0]:
                    pref = a[0] + b[1]

                if b[2] == b[0]:
                    suff = b[0] + a[2]

            return (length, pref, suff, best, a[4], b[5])

        def build(u, l, r):
            if l == r:
                tree[u] = (1, 1, 1, 1, s[l], s[l])
                return

            mid = (l + r) // 2

            build(u * 2, l, mid)
            build(u * 2 + 1, mid + 1, r)

            tree[u] = merge(tree[u * 2], tree[u * 2 + 1])

        def update(u, l, r, pos, c):
            if l == r:
                s[pos] = c
                tree[u] = (1, 1, 1, 1, c, c)
                return

            mid = (l + r) // 2

            if pos <= mid:
                update(u * 2, l, mid, pos, c)
            else:
                update(u * 2 + 1, mid + 1, r, pos, c)

            tree[u] = merge(tree[u * 2], tree[u * 2 + 1])

        build(1, 0, n - 1)

        ans = []

        for i, pos in enumerate(queryIndices):
            update(1, 0, n - 1, pos, queryCharacters[i])
            ans.append(tree[1][3])

        return ans
