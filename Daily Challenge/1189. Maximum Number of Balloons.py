#Came up with own
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = {}
        for ele in text:
            hashmap[ele] = hashmap.get(ele,0) + 1

        print(hashmap)

        count  = 0

        target = "balloon"
        n=len(target)
        i=0

        while target[i] in hashmap and hashmap[target[i]] > 0 :

            hashmap[target[i]] -= 1

            if i==n-1 :
                count +=1
                i=0

            else:
                i+=1


        return count





#other approach - just find the minimum of b a l o n occurance - l an o shouldbe //2 because it appears twice mininum of it half freq
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = [0] * 26

        for ch in text:
            freq[ord(ch) - ord('a')] += 1

        return min(
            freq[ord('b') - ord('a')],
            freq[ord('a') - ord('a')],
            freq[ord('l') - ord('a')] // 2,
            freq[ord('o') - ord('a')] // 2,
            freq[ord('n') - ord('a')]
        )
