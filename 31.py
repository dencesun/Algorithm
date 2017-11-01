class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)-1
        i = nums_len-1
        while i >= 0:
            if nums[i] < nums[i+1]:
                break;
            i = i - 1

        if i == -1:
            return nums.sort()

        n = i
        i = i+1
        max_pos = n+1
        while i <= nums_len:
            if nums[i] > nums[n] and nums[i] <= nums[max_pos]:
                max_pos = i
            i = i+1

        nums[n], nums[max_pos] = nums[max_pos], nums[n]
        n = n+1
        while n < nums_len:
            nums[n], nums[nums_len] = nums[nums_len], nums[n]
            n = n + 1
            nums_len = nums_len -1


# method2
# @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        n=len(nums)
        if n<2:
            return
        i,j,pLeft,pRight=n-2,n-1,-1,n-1
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i>=0:
            while j>i and nums[j]<=nums[i]:
                j-=1
            #must be j>i
            nums[i],nums[j]=nums[j],nums[i]
        pLeft=i+1
        while pLeft<pRight:
            nums[pLeft],nums[pRight]=nums[pRight],nums[pLeft]
            pLeft+=1


nums = [2, 3, 1, 3, 3]
test = Solution()
test.nextPermutation(nums)
print(nums)