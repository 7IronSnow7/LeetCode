# link = https://leetcode.com/problems/product-of-array-except-self/description/
#______________________
#      INFORMATION
#______________________

"""_summary_

238. Product of Array Except Self
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""
#______________________
#      SOLUTION
#______________________
from typing import List

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        
        # First pass: calculate products of all elements to the left
        left_product = 1
        for i in range(len(nums)):
            result[i] = left_product
            left_product *= nums[i]
            print(left_product)
        
        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right_product
            
            right_product *= nums[i]
            print(right_product)
        return result
            
            
        # Now result array contains products of all elements to the left
        # For [1,2,3,4], result would be [1,1,2,6]
        
        # Let's add the second pass...
        # What should we do to include products from the right?

solution = Solution()

print(solution.productExceptSelf([1, 2, 3, 4]))