#______________________
#      INFORMATION
#______________________

"""_summary_
Problem Description
You are given two strings, word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If one string is longer than the other, append the additional letters to the end of the merged string.

Return the merged string.

Examples
Example 1
Input:
word1 = "abc"
word2 = "pqr"

Output:
"apbqcr"

Explanation:
The merged string is formed as follows:
word1:  a   b   c  
word2:    p   q   r  
merged: a p b q c r

Example 2
Input:
word1 = "ab"
word2 = "pqrs"

Output:
"apbqrs"

Explanation:
Since word2 is longer, the remaining characters "rs" are appended to the end:
word1:  a   b  
word2:    p   q   r   s  
merged: a p b q   r   s

Example 3
Input:
word1 = "abcd"
word2 = "pq"

Output:
"apbqcd"

Explanation:
Since word1 is longer, the remaining characters "cd" are appended to the end:
word1:  a   b   c   d  
word2:    p   q  
merged: a p b q c   d

"""
#______________________
#      SOLUTION
#______________________

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string_length = len(word1 + word2)
        combined_words = ""
        i = 0
        
        while i < string_length:
            if i < len(word1):
                combined_words += word1[i]
            if i < len(word2):
                combined_words += word2[i]
            i += 1
        return combined_words
        
solution = Solution()
print(solution.mergeAlternately("ace", "bdfg"))

