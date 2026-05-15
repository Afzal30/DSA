class Solution:
    def findMin(self, nums: List[int]) -> int:
        def findpivot(num):
            start = 0
            end = len(num)-1
            while start<=end:
                mid = start + (end - start)//2
                if(mid<=len(num)-2 and num[mid]>num[mid+1]):
                    return mid
                elif( mid>0  and num[mid]<num[mid-1]):
                    return mid-1
                elif(num[mid] >=num[start]):
                    start = mid+1
                elif(num[mid] < num[start]):
                    end = mid-1
                        
            return end%len(num)

        peakindex = findpivot(nums)
        length = len(nums)-1

        if peakindex==length:
            return nums[0]
        else:
            return nums[peakindex+1]

        
