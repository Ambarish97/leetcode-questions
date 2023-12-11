# https://leetcode.com/problems/permutations

# Actual problem: find permutation of n given integer
# Sub problem: find permutation of n-1
# solution reference : https://www.youtube.com/watch?v=s7AvT7cGdSo


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        length = len(nums)

        # base case
        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
                if len(perm) == length:
                    result.append(perm)

            # result.extend(perms)
            nums.append(n)
        return result


if __name__ == '__main__':
    cost = [1, 2, 3]
    s = Solution()
    no = s.permute(cost)
    print("Output : ", no)
    