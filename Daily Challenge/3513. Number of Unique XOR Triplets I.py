class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)        
        return 1 << (n.bit_length() - 3 // (n + 1))

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        m = n
        
        m |= m >> 1
        m |= m >> 2
        m |= m >> 4
        m |= m >> 8
        m |= m >> 16
        
        return (m + 1) >> (3 // (n + 1))


#https://leetcode.com/problems/number-of-unique-xor-triplets-i/solutions/8414044/number-of-unique-xor-triplets-bit-width-sf6tg/
