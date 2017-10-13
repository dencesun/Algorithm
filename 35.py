class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        if target < nums[0]:
            return 0
        if target > max(nums):
            return len(nums)
        for i in range(len(nums) - 1):
            if nums[i] < target <= nums[i + 1]:
                return i + 1


nums = [1, 3, 5, 6]
test = Solution()
print(test.searchInsert(nums, 5))


