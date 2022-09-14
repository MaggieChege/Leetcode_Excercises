"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_map = {}

        for letter in magazine:
            letter_map[letter] = letter_map.get(letter, 0) + 1
        for letter in ransomNote:
            letter_map[letter] = letter_map.get(letter, 0) - 1
            if letter_map[letter] < 0:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct(ransomNote="aa", magazine="ab"))
    print(s.canConstruct(ransomNote="aa", magazine="aab"))
