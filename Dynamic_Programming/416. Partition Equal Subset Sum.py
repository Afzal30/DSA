#https://leetcode.com/problems/partition-equal-subset-sum/description/

class Solution:

    
    def helper(self,nums,target,index,cursum,flag,memo):

        if (index,cursum,flag) in memo:
            return memo[ (index,cursum,flag)]

        if flag:
            return flag 
            
        if len(nums)==index:
            return False

        if cursum == target:
            flag = True
        memo[ (index,cursum,flag)] =  self.helper(nums,target,index+1,cursum+nums[index],flag,memo) or self.helper(nums,target,index+1,cursum,flag,memo)
        return memo[ (index,cursum,flag)]

    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot%2 !=0 :
            return False
            
        else:
            memo = {}
            return self.helper(nums,tot//2,0,0,False,memo)
        
        
        
