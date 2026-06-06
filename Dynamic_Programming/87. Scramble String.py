#https://leetcode.com/problems/scramble-string/description/
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        if len(s1)!= len(s2):
            return False

        hashmap = {}
        
        def solve(a,b):
            if a==b:
                return True
            if len(a)<=1:
                return False
            n = len(a)
            flag = False

            if (a,b) in hashmap:
                return hashmap[(a,b)]
            for i in range(1,n):

              
                #conditon 1 : if swap is required, recusively compare the first partition of a, with the second partition of b
                if (a[0:i],b[n-i:n]) in hashmap:
                    cond_1_parti_1 =  hashmap[(a[0:i],b[n-i:n])]
                else:
                    cond_1_parti_1 = solve(a[0:i],b[n-i:n])
                    hashmap[a[0:i],b[n-i:n]] = cond_1_parti_1

                #conditon 1 : if swap is required, recusively compare the second partition of a, with the first partition of b
                if (a[i:n],b[0:n-i]) in hashmap:
                    cond_1_parti_2 =  hashmap[(a[i:n],b[0:n-i])]
                else:
                    cond_1_parti_2 = solve(a[i:n],b[0:n-i])
                    hashmap[(a[i:n],b[0:n-i])] = cond_1_parti_2

              #conditon 2: if swap is not required, recusivelycompare the first partition of a, with the first partition of b
                if (a[0:i],b[0:i]) in hashmap:
                    cond_2_parti_1 =  hashmap[(a[0:i],b[0:i])]
                else:
                    cond_2_parti_1 = solve(a[0:i],b[0:i])
                    hashmap[(a[0:i],b[0:i])] = cond_2_parti_1

                #conditon 1 : if swap is not required, recusively compare the second partition of a, with the second partition of b
                if (a[i:n],b[i:n]) in hashmap:
                    cond_2_parti_2 =  hashmap[(a[i:n],b[i:n])]
                else:
                    cond_2_parti_2 = solve(a[i:n],b[i:n])
                    hashmap[(a[i:n],b[i:n])] = cond_2_parti_2

                if (  cond_1_parti_1 and cond_1_parti_2 ) or (  cond_2_parti_1 and cond_2_parti_2):
                    flag = True
                    break

            return flag

        return solve(s1,s2)
            
        
