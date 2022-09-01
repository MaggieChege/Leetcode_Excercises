class Solution:
    def is_palindrome(self, x):
        str_ = str(x)
        if str_ == str_[::-1]:
            return True
        return False


if __name__ == "__main__":
    # begin
    s = Solution()
    print(s.is_palindrome(1001))
