class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        base = {1,2,3,4,5,6,7,8,9}
        output = []
        def sequential(n):
            if n<=10**9 :
                if n not in base:
                    output.append(n)
                rem = n%10
                prd = n*10
                #print(n,prd + rem + 1)
                if rem<9:
                    sequential(prd + rem + 1)
                

            else:
                return

        for ele in base:
            sequential(ele)

        sorted(output)
        #print(output)

        return sorted([ ele for ele in output if ele>=low and ele<=high] )



