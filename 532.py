import collections


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0 or len(nums)<=0:
            return 0
        if k == 0:
            counter = collections.Counter(nums)
            return sum(v > 1 for v in counter.values())
        if k > 0:
            return len(set(nums) & set(v+k for v in nums))


k = 2
nums = [3, 1, 4, 1, 5]

test = Solution()
print(test.findPairs(nums, k))