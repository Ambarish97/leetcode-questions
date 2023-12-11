# https://leetcode.com/problems/min-cost-climbing-stairs/
# (TLE solutions - not the most optimised solutions)

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)
        return Solution.minCostFn(self, cost, len(cost)-1)

    def minCostFn(self, cost, index):
        if index < 0:
            return 0
        return cost[index] + min(Solution.minCostFn(self, cost, index - 1), Solution.minCostFn(self, cost, index - 2))


if __name__ == '__main__':
    cost = [1,100,1,1,1,100,1,1,100,1]
    s = Solution()
    no = s.minCostClimbingStairs(cost)
    print("Output : ", no)
