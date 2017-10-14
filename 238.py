class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        n = nums.count(0)
        lens = len(nums)
        produce = 1
        for i in nums:
            if i != 0:
                produce *= i

        if n >= 2:
            ans = [0]*lens
        elif n == 1:
            ans = [0]*(lens-1)
            ans.insert(nums.index(0),produce)
            
        else:
            for i in nums:
                ans.append(produce/i)
        return ans

test = Solution()
print test.productExceptSelf([9,0,-2])
