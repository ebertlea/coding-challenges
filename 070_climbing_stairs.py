"""
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3: return n

        prev1=3
        prev2=2
        cur=0

        for _ in range(3,n):
            cur=prev1+prev2
            prev2=prev1
            prev1=cur
        return cur   
