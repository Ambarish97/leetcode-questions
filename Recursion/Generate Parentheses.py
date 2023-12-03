# https://leetcode.com/problems/generate-parentheses

# Actual problem: make n well-formed pair of parentheses
# Sub-problem: make 1,2,.....n-1,n pair of well-formed parentheses
# Bottom-up approach
# visualization: https://www.recursionvisualizer.com/?function_definition=def%20generator%28n%2CnumClosed%2CnumOpen%2CcurrString%2Cresult%29%3A%0A%20%20%20%20%20%20%20%20if%20numClosed%3D%3Dn%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20result.append%28currString%29%0A%20%20%20%20%20%20%20%20%20%20%20%20return%0A%20%20%20%20%20%20%20%20%23%20include%20close%0A%20%20%20%20%20%20%20%20if%20numOpen%3EnumClosed%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20generator%28n%2CnumClosed%2B1%2CnumOpen%2CcurrString%2B'%29'%2Cresult%29%0A%20%20%20%20%20%20%20%20%23%20include%20open%0A%20%20%20%20%20%20%20%20if%20numOpen%3Cn%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20generator%28n%2CnumClosed%2CnumOpen%2B1%2CcurrString%2B'%28'%2Cresult%29&function_call=generator%283%2C0%2C0%2C%22%22%2C%5B%5D%29
# time complexity = 2 power 2n (no of places to be filled is 2n)
# space complexity = 2n (height of tree)

class Solution:
    def generate_parenthesis(self, n: int) -> list[str]:
        ans = []
        Solution.helper(self, 0, 0, n, ans, "")
        return ans

    def helper(self, open, close, n, ans, curr):
        if close == n:
            ans.append(curr)
            return

        # add closing parentheses
        if close < open:
            Solution.helper(self, open, close + 1, n, ans, curr+')')

        # add opening parentheses
        if open < n:
            Solution.helper(self, open + 1, close, n, ans, curr+'(')


if __name__ == '__main__':
    nums = 3
    s = Solution()
    ans = s.generate_parenthesis(nums)
    print(ans)
