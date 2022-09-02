from typing import List


class Solution:
    """
    Given a sorted array of distinct integers and a target value,
    return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        l = int(0)
        r = len(nums) - 1
        while l < r:
            mid = int((l + r) / 2)
            # breakpoint()
            print(mid, "mid")
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] < target:
            return l + 1
        return l


if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert(nums=[1, 3, 5, 6], target=2))
