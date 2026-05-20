class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        #common = 0
        #common_set = {}
        res = []
        for i in range(len(A)):
            list1 = A[:i+1]
            list2 = B[:i+1]
            common = list(set(list1) & set(list2))
            res.append(len(common))
        return res

        
