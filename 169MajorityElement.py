import collections

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ndict = collections.Counter(nums)
        nlen = len(nums)
        for key, values in ndict.items():
        	if values > (nlen/2):
        		return key

test = Solution()
print test.majorityElement([1,1,1,2])