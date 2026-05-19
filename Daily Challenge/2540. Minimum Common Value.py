class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=0
        j = 0
        #nums1=list(set(nums1))
        #nums2=list(set(nums2))
        while (i<len(nums1) and  j<len(nums2)):
            print(",j ",i,j)
            print(nums1[i],nums2[j])
            if nums1[i]==nums2[j]:
                return nums1[i]
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1

        
        return -1
