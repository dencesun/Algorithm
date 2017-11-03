class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = dict()

        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i

        # print(dic)
        return False


nums = [-1, -1, 2]
k = 2
test = Solution()
print(test.containsNearbyDuplicate(nums, k))
