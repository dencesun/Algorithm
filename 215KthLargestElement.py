class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = [-2147483648]*k
        for i in nums:
            if i > ans[0]:
                ans[0] = i
                ans.sort()
        return ans[0]