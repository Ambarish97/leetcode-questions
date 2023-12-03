class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subset = []
        index = 0
        curr_subset = []
        Solution.helper(self, nums, subset, index, curr_subset)
        return subset

    def helper(self, nums, subset, index, curr_subset):
        if index == len(nums):
            subset.append(curr_subset.copy())
            curr_subset = []
            return

        # exclude element
        Solution.helper(self, nums, subset, index + 1, curr_subset)

        # include element
        curr_subset.append(nums[index])
        Solution.helper(self, nums, subset, index + 1, curr_subset)
        curr_subset.pop()

if __name__ == '__main__':
    nums = [1,2,3]
    # nums = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81,
    #  185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]
    s = Solution()
    no = s.subsets(nums)
    print(no)

