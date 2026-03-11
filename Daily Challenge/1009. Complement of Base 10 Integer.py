class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binn = bin(n)[2:]
        mask = "1"*len(binn)
        return int(binn,2)^int(mask,2)
        
