class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def count_peak_valley(n):
            
            s = str(n)
            length = len(s)
            if length<=2:
                return 0
            count=0
            for i in range(1,length-1):
                left = int(s[i-1])
                right = int(s[i+1])
                ele = int(s[i])
                #print(n,ele,left,right)

                if ele<left and ele<right:
                    count+=1
                elif ele>left and ele>right:
                    count+=1
                else:
                    continue

            #print(n,count)
            return count

        ans = 0
        for i in range(num1,num2+1):
            ans +=count_peak_valley(i)

        return ans




        
