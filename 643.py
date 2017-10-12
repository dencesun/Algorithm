class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) >= k:
            max_average = sum(nums[0:k])
        cur = max_average

        i = 0
        j = k
        l = len(nums)
        while j < l:
            cur = cur + nums[j] -nums[i]
            j = j+1
            i = i+1
            max_average = max(max_average, cur)
        return float(max_average)/k


nums = [1, 12, -5, -6, 50, 3]
test = Solution()
print(test.findMaxAverage(nums, 4))