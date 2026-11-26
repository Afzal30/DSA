class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        elif n== 10:
            return True
        else:
            curr = n-10
            req = 9
            count = 1
            alice = True
            while curr >= req:
                if count % 2 == 0:
                    alice = True
                else:
                    alice = False
                curr = curr - req
                req -=1
                count+=1
            return alice




        
