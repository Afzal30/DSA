class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        temp = ""

        if s == goal:
            return True

        for i in range(len(s)):
            first = s[i+1:]
            second = s[:i+1]
            print(i, first + second)

            if first + second == goal:
                return True

        return False

        
