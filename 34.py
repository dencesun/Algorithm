class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # method1 超时
        # start = nums.index(target)
        # end = start
        # while end < len(nums) and nums[end] == target:
        #     end += 1
        #
        # return [start, end-1]

        # method2 提交通过，但不是最好的方法
        # if not nums:
        #     return [-1, -1]
        # pleft, pright = 0, len(nums)-1
        # while pleft <= pright:
        #     median = int((pleft+pright)/2)
        #     if nums[median]<target:
        #         pleft = median+1
        #     elif nums[median] > target:
        #         pright = median-1
        #     else:
        #         break;
        # if pleft>pright:
        #     return [-1, -1]
        # start, end, pleft, pright = median, median, median, median
        # while pleft >= 0:
        #     if nums[pleft] == target:
        #         start = pleft
        #         pleft -= 1
        #     else:
        #         break;
        # while pright <= len(nums)-1:
        #     if nums[pright] == target:
        #         end = pright
        #         pright += 1
        #     else:
        #         break;
        # return [start, end]

    # method3
        def search(pleft, pright, target):
            while pleft <= pright:
                median = int((pleft+pright)/2)
                if nums[median] >= target:
                    pright = median - 1
                else:
                    pleft = median + 1

            return pleft
        if not nums:
            return [-1, -1]
        pleft = search(0, len(nums)-1, target)
        pright = search(0, len(nums)-1, target+1)
        if pleft <= (pright-1) < len(nums):
            return [pleft, pright-1]
        else:
            return [-1, -1]







nums = [5, 7, 7, 8, 8, 10]
nums1 = [1]
target = 8
target1 = 0
test = Solution()
print(test.searchRange(nums1, target1))