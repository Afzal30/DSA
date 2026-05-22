class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findmax(num):
            if len(num)==1:
                return 0
            start=0
            end = len(num)-1
            while(start<=end):
                mid = start + (end-start)//2
                
                if(mid<=len(num)-2 and num[mid]>num[mid+1]):
                    return mid
                elif(num[mid]<num[mid-1]):
                    return mid-1
                elif(num[mid] >=num[start]):
                    start = mid+1
                elif(num[mid] < num[start]):
                    end = mid-1
                #else:
                #   start = start+1
            return end
                
        #peakelementindex = nums.index(max(nums))
        peakelementindex =findmax(nums)
        print(peakelementindex)
        def incpart(nums,peakelementindex):
            start = 0
            end = peakelementindex
            while(start <= end):
                mid = start + (end-start)//2
                if(nums[mid]>target):
                    end= mid-1
                elif(nums[mid] < target):
                    start = mid+1
                else:
                    return mid
            return -1

        ans = incpart(nums,peakelementindex)
        if ans==-1:
            
            start = peakelementindex+1
            end = len(nums)-1
            while(start <= end):
                mid = start + (end-start)//2
                if(nums[mid]<target):
                    start = mid+1
                elif(nums[mid] > target):
                    end = mid-1
                else:
                    return mid
            return -1
        return ans
