class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessthan = []
        greaterthan=[]
        pivots = []

        for ele in nums:

            if ele<pivot:
                lessthan.append(ele)

            elif ele>pivot:
                greaterthan.append(ele)

            else:
                pivots.append(ele)

        return lessthan + pivots + greaterthan


        
