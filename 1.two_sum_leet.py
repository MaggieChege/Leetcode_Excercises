class Solution:
    def twoSum(self, num, target):
        val = [(v, k) for k, v in enumerate(num)]
        print(val)
        begin = 0
        end = len(num) - 1

        while begin < end:
            curr_value = val[begin][0] + val[end][0]

            if curr_value == target:
                return [val[begin][1], val[end][1]]
            elif curr_value < target:
                begin += 1
            else:
                end -= 1


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([3, 2, 4], 5))
