class Solution:
    def minOperations(self, s: str) -> int:
        sorted_s = sorted(s)
        mn = sorted_s[0]
        mx = sorted_s[-1]
        ss = "".join(sorted_s)
        print(ss)
        print(s)
        if ss == s:
            return 0
        elif len(s) == 2:
            return -1
        elif s.find(mn) == 0 or s[::-1].find(mx)==0:
            return 1
        elif (s.count(mx) ==1 and s.find(mx) == 0 ) and (s.count(mn) ==1 and s.find(mn) == len(s)-1 ):
            return 3
        else:
            return 2
        
