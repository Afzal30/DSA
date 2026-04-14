#https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        dict1= {}
        dict2= {}

        for ele in s:
            if ele in dict1:
                dict1[ele]+=1
            else:
                dict1[ele]=1

        for ele in t:
            if ele in dict2:
                dict2[ele]+=1
            else:
                dict2[ele]=1

        for k,v in dict1.items():
            if k not in dict2 or dict2[k] != v:
                return False

        return True

#space optimization using single dictionary
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        dict1= {}

        for ele in s:
            if ele in dict1:
                dict1[ele]+=1
            else:
                dict1[ele]=1

        for ele in t:
            if ele not in dict1:
                return False
            
            dict1[ele]-=1
            if dict1[ele]==0:
                del dict1[ele]

        
        return len(dict1)==0

        
        
        
#using alg/lib

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        
        
        
        
