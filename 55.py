class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        n = nums[0]
        i = 1
        while i < len(nums) and n >=i:
            if nums[i] + i > n:
                n = nums[i] + i
            i = i+1

        return n >= len(nums)-1


nums = [2, 3, 1, 1, 4]
nums1 = [3, 2, 1, 0, 4]
test = Solution()
print(test.canJump(nums1))
