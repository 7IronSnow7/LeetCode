# link: https://leetcode.com/problems/longest-common-prefix/description/
#______________________
#      INFORMATION
#______________________

"""_summary_
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
#______________________
#      SOLUTION
#______________________
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for c in zip(*strs):
            if len(set(c)) == 1:
                prefix += c[0]
            else:
                break
        
        return prefix
    
solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
