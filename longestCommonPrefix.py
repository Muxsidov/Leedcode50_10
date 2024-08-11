# My solution to Longest common prefix problem from Leetcode https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        return_str = ""

        # Find the length of the shortest string
        min_length = min(len(s) for s in strs)

        for count in range(min_length):
            for word in strs:
                if strs[0][count] == word[count]:
                    continue
                else:
                    return return_str
            return_str += str(strs[0][count])
        return return_str
