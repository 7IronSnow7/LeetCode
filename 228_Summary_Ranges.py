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
# class Solution:
#     def summaryRanges(self, nums: List[int]) -> List[str]:
#         # handle empty array
#         if not nums:
#             return []

#         result = []
#         start = nums[0]

#         for i in range(len(nums)):
#             # Check if we are at the end or if there is a gap
#             if i == len(nums) - 1 or nums[i+1] - nums[i] > 1:
#                 # If start and current number are the same
#                 if start == nums[i]:
#                     result.append(str(start))
#                 # If we have a sequence
#                 else:
#                     result.append(f"{start}->{nums[i]}")

#                 # Start new sequence if not at the end 
#                 if i < len(nums) - 1:
#                     start = nums[i +1]
        
#         return result
# solution = Solution()
# print(solution.summaryRanges([0,1,2,4,5,7]))
# print(solution.summaryRanges([0,2,3,4,6,8,9]))
# import functools

# def find_longest(word_so_far, next_word):
#     # Your code here - compare lengths and return the longer word
#     if len(word_so_far) < len(next_word):
#         return next_word
#     return word_so_far

# words = ["cat", "elephant", "mouse", "hippopotamus", "dog"]
# longest_word = functools.reduce(find_longest, words)
# print(longest_word)
# # Use reduce to find the longest word
# import functools

# def concat_with_separator(accumulated, next_string, sep=" | "):
#     # Your code here - join strings with separator
#     return accumulated + sep + next_string

# strings = ["hello", "world", "python"]
# # Use reduce to join them
# joined_strings = functools.reduce(concat_with_separator, strings)
# print(joined_strings)
# import functools

# def find_max(max_so_far, next_num):
#     # Your code here - compare and return larger number
#     if max_so_far < next_num:
#         return next_num
#     return max_so_far

# numbers = [5, 12, 3, 8, 9, 1]
# # Use reduce to find max
# max_number = functools.reduce(find_max, numbers)
# print(max_number)

import functools

books = [
    {"title": "The Hobbit", "author": "Tolkien", "pages": 295},
    {"title": "Dune", "author": "Herbert", "pages": 412},
    {"title": "The Guide", "author": "Adams", "pages": 224},
    {"title": "Snow Crash", "author": "Stephenson", "pages": 470},
]

def find_longest_book(book_so_far, next_book): 
    # Your code here!
    if book_so_far["pages"] < next_book["pages"]:
        return next_book
    return book_so_far

most_pages = functools.reduce(find_longest_book, books[1:], books[0])
print(most_pages)

    # Compare pages and return the book with more pages
    # But be careful! book_so_far will be a dictionary

# Should output something like: "Snow Crash by Stephenson (470 pages)"