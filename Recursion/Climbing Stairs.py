class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        else:
            return Solution.climbStairs(self, n - 1) + Solution.climbStairs(self, n - 2)
