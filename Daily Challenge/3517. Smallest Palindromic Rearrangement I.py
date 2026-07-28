from collections import Counter

class Solution1:
    def smallestPalindrome(self, s: str) -> str:
        counts = Counter(s)
        ans = ""
        odd = ""
        
        for ch in sorted(counts.keys()):
            if counts[ch] % 2 != 0:
                odd = ch
            ans += ch * (counts[ch] // 2)
            
        return ans + odd + ans[::-1]
