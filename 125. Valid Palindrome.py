"""
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

import re


class Solution:
    def isPalindrome(self, s: str, target: bool) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        new_string = re.sub(r"[^\w\s]", "", s)

        if new_string == new_string[::-1]:
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(s="race a car", target=False))
    print(s.isPalindrome(s="A man, a plan, a canal: Panama", target=True))
