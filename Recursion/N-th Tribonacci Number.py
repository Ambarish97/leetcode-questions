# https://leetcode.com/problems/n-th-tribonacci-number/
# (TLE solutions - not the most optimised solutions)

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1
        elif n == 0:
            return 0
        else:
            return Solution.tribonacci(self, n - 3) + Solution.tribonacci(self, n - 2) + Solution.tribonacci(self,
                                                                                                             n - 1)
