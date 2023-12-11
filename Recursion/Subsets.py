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
    nums = [1, 2, 3]
    s = Solution()
    no = s.subsets(nums)
    print("Output : ", no)

