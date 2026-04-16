#https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for ele in hashset:
            if ele-1 not in hashset:
                length =1
                curr = ele

                while curr+1 in hashset:
                    curr+=1
                    length+=1

                longest = max(longest,length)

        return longest
                    

                    
        return max(hashmap.values()) if hashmap else 0



        
