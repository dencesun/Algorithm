from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # ans = []
        # nums.sort()
        # for i in nums:
        # 	if i not in nums[nums.index(i)+1:]:
        # 		if i not in ans:
        # 			ans.append(i)
        ans = []
        count = Counter(nums)
        for k,v in count.items():
        	if v == 1:
        		ans.append(k)
        return ans

test = Solution()
print test.singleNumber([1,2,3,5,5,3,2])