class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        dp = list()
        dp.append(nums[0])
        for i in range(1, len(nums)):
            dp.append(max(dp[i-1]+nums[i], nums[i]))

        return max(dp)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
test = Solution()
print(test.maxSubArray(nums))
