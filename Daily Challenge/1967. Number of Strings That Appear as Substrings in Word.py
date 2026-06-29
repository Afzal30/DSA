class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for ele in patterns:
            if ele in word:
                count+=1

        return count


#sliding window approach
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pat in patterns:
            left, right = 0, len(pat)
            while right <= len(word):
                if pat == word[left:right]:
                    count += 1
                    break
                left += 1
                right += 1

        return count
        
