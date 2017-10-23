class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        left = 0
        right = len(nums)-1

        while left < right-1:
            mid = (left + right)/2
            if nums[mid]>nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid-1]:
                right = mid - 1
            else:
                left = mid + 1

        return left if nums[left] > nums[right] else right