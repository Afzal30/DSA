#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        for i in range(len(s)):
            temp = s[i]
            for j in range(i+1,len(s)):
                if s[j] in temp:
                    break
                else:
                    temp += s[j]
            maxlength = max(maxlength,len(temp))

        return maxlength


##sliding window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        seen = set()
        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            maxlength = max(maxlength,right-left+1)

        return maxlength


        
