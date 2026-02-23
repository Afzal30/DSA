class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        st = set()

        for i in range(n - k + 1):
            st.add(s[i:i+k])

        return len(st) == (1 << k)
