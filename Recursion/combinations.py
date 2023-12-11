# https//leetcode.com/problems/combinations

# Actaul problem: make combinations of n numbers.
# Sub problem: make combinations of n-1(top down) numbers or 1,2....n-1,n numbers(bottom-up).

# Bottom-up approach

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        curr = []
        Solution.helper(self, n, k, 1, curr, result)
        return result

    def helper(self, n, k, index, curr, result):
        if k == 0:
            result.append(curr.copy())
            return

        if index == n+1:
            return

        # don't pick
        self.helper(n, k, index+1, curr, result)

        # pick
        curr.append(index)
        self.helper(n, k - 1, index + 1, curr, result)
        curr.pop()


if __name__ == '__main__':
    nums = 4
    print("Input : ", nums)
    s = Solution()
    a = s.combine(nums, 2)
    print("Output : ", a)
