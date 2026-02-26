#My solution
class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        while s!='1':
            s = int(s,2)
            if s%2 == 0:
                s //=2
            else:
                s +=1

            s = bin(s)[2:]
            steps +=1

        return steps
        
