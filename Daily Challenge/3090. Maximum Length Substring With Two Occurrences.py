#brute force approach
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_count = float('-inf')
        for i in range(len(s)):
            for j in range(i, len(s)):
                ele = s[i:j+1]

                if len(ele)<=max_count:
                    continue
                for ch in ele:
                    if ele.count(ch)>2:
                        break
                else:
                    max_count = max(max_count,len(ele))

        



        return max_count

            
#sliding window
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        result = 0
        start = 0

        storage = {}

        for end in range(len(s)):
            storage[s[end]] = storage.get(s[end], 0) + 1

            # Shrink window if frequency exceeds 2
            while storage[s[end]] > 2:
                storage[s[start]] -= 1
                start += 1

            result = max(result, end - start + 1)

        return result
