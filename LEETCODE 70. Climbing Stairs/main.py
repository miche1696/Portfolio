class Solution:
    def climbStairs(self, n: int) -> int:
        j = 1
        i = 0
        count = 0
        while (True):
            if count == n+1:
                return i
            temp = i
            i = j
            j = temp + j
            count = count+1
            
""" Non optimized solution
class Solution:
    def recursiveClimb(self, r : int) -> int:
        if r==0 or r==1:
            return 1
        else:
            return self.recursiveClimb(r-1) + self.recursiveClimb(r-2)
    
    def climbStairs(self, n: int) -> int:
        return self.recursiveClimb(n)
"""