# link: https://leetcode.com/problems/summary-ranges/description/
#______________________
#      INFORMATION
#______________________

"""_summary_
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
"""
#______________________
#      SOLUTION
#______________________
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # handle empty array
        if not nums:
            return []

        result = []
        start = nums[0]

        for i in range(len(nums)):
            # Check if we are at the end or if there is a gap
            if i == len(nums) - 1 or nums[i+1] - nums[i] > 1:
                # If start and current number are the same
                if start == nums[i]:
                    result.append(str(start))
                # If we have a sequence
                else:
                    result.append(f"{start}->{nums[i]}")

                # Start new sequence if not at the end 
                if i < len(nums) - 1:
                    start = nums[i +1]
        
        return result
solution = Solution()
print(solution.summaryRanges([0,1,2,4,5,7]))
print(solution.summaryRanges([0,2,3,4,6,8,9]))
import functools

