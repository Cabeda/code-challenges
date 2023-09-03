# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0

        for i in range(len(s)):
            letters = set()
            for j in range(i, len(s)):
                if s[j] in letters:
                    if len(letters) > maxLength:
                        maxLength = len(letters)
                    break
                else:
                    letters.add(s[j])

                if len(letters) > maxLength:
                    maxLength = len(letters)

        return maxLength


sol = Solution()

