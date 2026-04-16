#https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        res = []
        for m in strs:
            ele = "".join(sorted(m))
            if ele in mydict:
                mydict[ele].append(m)
            else:
                mydict[ele]=[m]

        for value in mydict.values():
            res.append(value)

        return res


        
