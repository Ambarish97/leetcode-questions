# https://leetcode.com/problems/house-robber-ii
# (TLE solutions - not the most optimised solutions)

# Actual problem: rob houses, but don't rob adjacent houses and first and last house together
# Sub-problem: If we rob nth house then we either rob n+2 house. If we don't rob nth then we rob n+1 or n+3

# Top-down approach(n to 0)
# Reccurence relation: f(n)=max(num[n]+n-2,n-1)

class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(self.rob_house(nums, len(nums) - 1, 1), self.rob_house(nums, len(nums) - 2, 0))

    def rob_house(self, nums: list[int], index: int, stop: int) -> int:
        if index < stop:  # base condition
            return 0
        include = nums[index] + self.rob_house(nums, index - 2, stop)
        exclude = self.rob_house(nums, index - 1, stop)
        return max(include, exclude)

    def rob_2(self, nums: list[int]) -> int:
        index = 0
        flag = 0
        return max(Solution.helper(self, nums, index, flag), Solution.helper(self, nums, index + 1, flag))

    def helper(self, nums, index, flag):
        if index >= len(nums):
            return 0

        # rob the house
        if index == 0:
            flag = 1
            return max(nums[index] + Solution.helper(self, nums, index + 2, flag),
                       Solution.helper(self, nums, index + 1, flag))
            flag = 0
        elif not (index == len(nums) - 1 and flag == 1):
            return max(nums[index] + Solution.helper(self, nums, index + 2, flag),
                       Solution.helper(self, nums, index + 1, flag))

        # don't rob the house
        return max(Solution.helper(self, nums, index + 1, flag), Solution.helper(self, nums, index + 1, flag))
