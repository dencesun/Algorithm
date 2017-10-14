class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)-k%len(nums)
        nums[:] = nums[k:]+nums[:k]
test = Solution()
nums = [1,2,3,4,5,6,7]
test.rotate(nums,3)
print nums
