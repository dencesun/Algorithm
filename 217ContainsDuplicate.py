import collections

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        collectnum = collections.Counter(nums)
        if len(nums) == 0: return False
        for key, values in collectnum.items():
        	if collectnum[key]>=2:
        		return True 
        return False

test = Solution()
print test.containsDuplicate([1,2,2])
print test.containsDuplicate([2,2,2])
print test.containsDuplicate([1,2,3,1])
print test.containsDuplicate([])