class Solution:
    def fib(self, n: int) -> int:
        if 0 <= n <= 30:
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return Solution.fib(self, n - 1) + Solution.fib(self, n - 2)
