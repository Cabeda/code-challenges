import re

# https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. Must also accept incepted parentheses like "({})". It must always close the last opened bracket. Must match the entire string.

class Solution:
    def isValid(self, s: str) -> bool:

        length = len(s)
        while length > 0:
            shortened = re.sub(r'\(\)|\[\]|\{\}', '', s)
            if shortened == s:
                return False
            length = len(shortened)
            s = shortened

        
        return True
