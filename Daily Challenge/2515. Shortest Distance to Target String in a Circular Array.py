class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        for i in range((n >> 1) + 1):
            if ((words[(startIndex + i) % n] == target) |
                (words[(startIndex - i) % n] == target)):
                return i
        return -1

        
                
        
