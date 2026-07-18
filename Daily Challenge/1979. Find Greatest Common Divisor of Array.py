class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            if b==0:
                return a
            else:
                return gcd(b,a%b)
        

        return gcd(min(nums),max(nums))

#without recursion - effective approach
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = float('inf')
        mx = float('-inf')
        for ele in nums:
            if ele < mn:
                mn = ele
            if ele > mx:
                mx = ele

        #print(mn,mx)
        for i in range(mn,0,-1):
            #print(i)
            if mn% i==0 and mx%i == 0:
                return i
