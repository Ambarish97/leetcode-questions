class Solution:
    def rob(self, nums: list[int]) -> int:
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

