class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans=len(arr1)
        for ele in arr1:
            for item in arr2:
                if abs(ele - item) <= d:
                    ans-=1
                    break
            
        return ans
        
