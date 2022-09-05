"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

#30daysofcoding
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :type: bool
        """
        if s is None:
            return True
        if len(s) % 2 != 0:
            return False

        new_str = s.replace("{}", "").replace("()", "").replace("[]", "")
        if len(new_str) > 0:
            return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isValid(s="()[]}"))
