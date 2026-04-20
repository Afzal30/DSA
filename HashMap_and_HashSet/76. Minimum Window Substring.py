#https://leetcode.com/problems/minimum-window-substring/
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t or len(s)<len(t):
            return ""

        char_count = {}
        for char in t:
            char_count[char] = char_count.get(char,0) + 1

        required = len(char_count)
        formed = 0

        left,right = 0,0
        min_length = float('inf')
        window_count = {}
        result = ""

        while right<len(s):
            char = s[right]
            window_count[char] = window_count.get(char,0)+1

            if char in char_count and window_count[char] == char_count[char]:
                formed+=1

            while left<=right and formed == required:
                char = s[left]

                if right-left+1 < min_length:
                    min_length = right-left+1
                    result = s[left:right+1]

                window_count[char] -=1

                if char in char_count and window_count[char]<char_count[char]:
                    formed -= 1

                left +=1

            right +=1


        return result

                








        
        
        
