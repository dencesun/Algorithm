class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # time limited
        # if not nums:
        #     return
        #
        # nums_len = len(nums)
        # for i in range(nums_len-1):
        #     j = nums_len-1
        #     while j > i:
        #         if nums[j] <= nums[j-1]:
        #             nums[j], nums[j-1] = nums[j-1], nums[j]
        #             # print(nums)
        #             j -= 1 c

        # method2
        if not nums:
            return
        cnt = list([0])*3

        for i in nums:
            cnt[i] += 1
        j = 0
        # print(cnt)
        for i in range(len(nums)):
            while cnt[j] == 0 and j < 3:
                j += 1
            nums[i] = j
            cnt[j] -= 1
            # print(nums)


nums = [2, 0]

test = Solution()
test.sortColors(nums)
print(nums)
