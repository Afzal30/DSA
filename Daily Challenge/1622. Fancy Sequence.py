class Fancy:

    def __init__(self):
        self.lst = []
        self.add = 0
        self.mul = 1
        

    def append(self, val: int) -> None:
        x = (val - self.add +   (10**9 + 7 ))  % (10**9 + 7 )
        self.lst.append(x * pow(self.mul,  (10**9 + 7 ) -2,  (10**9 + 7 ) ) %   (10**9 + 7 ) )
        

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc)  % (10**9 + 7 )
        

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m)  % (10**9 + 7 )
        self.add = (self.add * m)  % (10**9 + 7 )
        

    def getIndex(self, idx: int) -> int:
        if idx < len(self.lst):
            return (self.mul * self.lst[idx] + self.add)% (10**9 + 7 )

        else:
            return -1
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
