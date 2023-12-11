# https://leetcode.com/problems/decode-ways/description/
# (TLE solutions - not the most optimised solutions)

# Actual problem: Decode string of n characters
# Sub-problem: Decode string of n-1,n-2,.....1,0 characters
# Bottom up approach (0 to n)
# Visualization: https://www.recursionvisualizer.com/?function_definition=def%20decodeString%28index%2CinputString%29-%3Eint%3A%0A%20%20%20%20%20%20%20%20if%20index%3C%3D0%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20%20%20%20%20result%3D0%0A%20%20%20%20%20%20%20%20if%20inputString%5Bindex%5D!%3D'0'%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20result%3DdecodeString%28index-1%2CinputString%29%0A%20%20%20%20%20%20%20%20if%20%28inputString%5Bindex-1%5D%3D%3D'1'%20or%20%28inputString%5Bindex-1%5D%3D%3D'2'%20and%20inputString%5Bindex%5D%3E%3D'0'%20and%20inputString%5Bindex%5D%3C%3D'6'%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20result%2B%3DdecodeString%28index-2%2CinputString%29%0A%20%20%20%20%20%20%20%20return%20result&function_call=decodeString%283%2C%221111%22%29

class Solution:
    def numDecodings(self, s: str) -> int:
        # return 0 as leading zero is present
        if "0" == s[0]:
            return 0
        curr = ""
        ans = []
        index = 0
        Solution.helper(self, s, curr, ans, index)
        return len(ans)

    def helper(self, s, curr, ans, index):
        # base condition
        if index == len(s):
            ans.append(curr)
            return

        # if double-digit or single digit does not start with zero
        if s[index] != "0":
            # condition for double digits
            if index <= len(s) - 2 and 0 < int(s[index:index + 2]) <= 26:
                # converting string number to alphabet and adding the alphabet to curr
                curr = curr + chr(int(s[index:index + 2]) + 64)
                Solution.helper(self, s, curr, ans, index + 2)
                curr = curr.rstrip(curr[-1])

            # code for single digit
            curr = curr + chr(int(s[index]) + 64)
            Solution.helper(self, s, curr, ans, index + 1)
            curr = curr.rstrip(curr[-1])


if __name__ == '__main__':
    nums = "2101"
    s = Solution()
    ans = s.numDecodings(nums)
    print("Output : ", ans)
