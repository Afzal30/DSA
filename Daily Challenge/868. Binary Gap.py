class Solution:
    def binaryGap(self, n: int) -> int:
        binn = bin(n)[2:]
        if binn.count('1')==1:
            return 0
        lst = [i for i, ltr in enumerate(binn) if ltr == '1']
        maxi = float('-inf')
        for i in range(len(lst)-1):
            if lst[i+1]-lst[i] > maxi:
                maxi = lst[i+1]-lst[i] 
        return maxi
