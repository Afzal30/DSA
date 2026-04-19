#https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []

        left = 0
        res = []
        counter_p = Counter(p)
        window = Counter(s[:len(p)])

        if window ==counter_p:
            res.append(0)

        for right in range(len(p),len(s)):
            window[s[right]] += 1
            window[s[left]] -=1

            if window[s[left]] == 0:
                del window[s[left]]

            left +=1

            if window == counter_p:
                res.append(left)

        return res

        
