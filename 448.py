class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max_len = len(nums)
        if max_len == 0:
            return []
        ans = list(set(range(1, max_len+1))-set(nums))
        return ans


nums = [1,1]
test = Solution()
print(test.findDisappearedNumbers(nums))

