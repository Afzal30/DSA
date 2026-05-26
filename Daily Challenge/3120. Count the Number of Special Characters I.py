class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        visited = set()
        for ele in word:
            #print(visited)
            #print(count)
            if ele not in visited:
                #print(ele)
                visited.add(ele)
                if ele.isupper():
                    if ele.lower() in word:
                        visited.add(ele.lower())
                        count+=1
                else:
                    if ele.upper() in word:
                        visited.add(ele.upper())
                        count+=1

        return count

        
