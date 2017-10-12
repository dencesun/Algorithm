class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        i = 0
        while i < len(nums):
            cur = 0
            while (i+1) < len(nums) and nums[i] < nums[i+1]:
                cur = cur + 1
                i = i+1
            i = i+1
            cur = cur + 1
            max_len = max(cur, max_len)

        return max_len


nums = [2, 2, 2]

test = Solution()
print(test.findLengthOfLCIS(nums))