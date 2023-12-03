class Solution:
    def rob(self, nums: list[int]) -> int:
        index = 0
        return max(nums[index]+Solution.helper(self, nums, index+2), Solution.helper(self, nums, index+1)
)

    def helper(self, nums: list[int], index):
        if index >= len(nums):
            return 0
        else:
            return max(nums[index]+Solution.helper(self, nums, index+2), Solution.helper(self, nums, index+1))


if __name__ == '__main__':
    # nums = [1, 2, 3, 1]
    nums = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81,
     185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]
    s = Solution()
    no = s.rob(nums)
    print(no)
