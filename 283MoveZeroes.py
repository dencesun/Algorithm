class Solution(object):
    def moveZeroes(self, nums):
    	index = 0
    	lens = len(nums)
    	for x in range(lens):
    		if nums[x] != 0:
    			nums[index] = nums[x]
    			index = index +1
    		else:
    			continue
    	while index < lens:
    		nums[index] = 0
    		index = index+1
    	return nums

test = Solution()
nums = [0,1,0,3,12]
print test.moveZeroes(nums)