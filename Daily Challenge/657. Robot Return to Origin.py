#657. Robot Return to Origin

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        up,down,left,right = 0,0,0,0
        for ele in moves:
            if ele == "U":
                up+=1
            elif ele == "D":
                down+=1
            elif ele == "L":
                left+=1
            else:
                right+=1

        return up==down and left==right


#approach two

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) & 1: return False
        f = Counter(moves)
        return f['U'] == f['D'] and f['L'] == f['R']
