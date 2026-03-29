#OWN solution

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        a1 = s1[2]+s1[1]+s1[0]+s1[3]
        a2 = s1[0]+s1[3]+s1[2]+s1[1]
        b1 = s2[2]+s2[1]+s2[0]+s2[3]
        b2 = s2[0]+s2[3]+s2[2]+s2[1]

        print(a1,a2,b1,b2,s1,s2)
        if a1 == s2 or a2 == s2:
            return True
        elif b2 == s1 or b1 ==s1:
            return True

        elif a1[0]+a1[3]+a1[2]+a1[1] == s2:
            return True
        elif b1[0]+b1[3]+b1[2]+b1[1] == s1:
            return True

        else:
            return False

##leetcode solution, more effecive

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return ((s1[0] == s2[0] and s1[2] == s2[2]) or
                (s1[0] == s2[2] and s1[2] == s2[0])) and \
               ((s1[1] == s2[1] and s1[3] == s2[3]) or
                (s1[1] == s2[3] and s1[3] == s2[1]))
