class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                cnt += 1
                if i == 0:
                    nums[i+1] = nums[i]
                elif nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i-1]
                else:
                    nums[i+1] = nums[i]
        return cnt > 1


nums = [4, 2, 2, 1]
test = Solution()
print(test.checkPossibility(nums))