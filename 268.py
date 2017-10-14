class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        lens = len(nums)
        
        for i in range(lens):
        	if i != nums[i]:
        		return i
       	return i
test = Solution()
print test.missingNumber([0,1])
