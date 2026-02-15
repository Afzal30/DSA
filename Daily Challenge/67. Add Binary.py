class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        print(a)
        b = int(b,2)
        print(b)
        return bin(a+b)[2:]
        
