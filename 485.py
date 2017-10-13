# Method1
# class Solution(object):
#     def findMaxConsecutiveOnes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         max_consecutive = 0
#
#         i = 0
#         while i < len(nums):
#             curr = 0
#             while nums[i] == 1:
#                 curr += 1
#                 i += 1
#                 if i == len(nums):
#                     break
#             i = i+1
#             max_consecutive = max(curr, max_consecutive)
#
#         return max_consecutive


# Method2
# class Solution(object):
#     def findMaxConsecutiveOnes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         max_consecutive = 0
#         curr = 0
#         for i in nums:
#             if i == 1:
#                 curr += 1
#             else:
#                 max_consecutive = max(max_consecutive, curr)
#                 curr = 0
#
#         max_consecutive = max(max_consecutive, curr)
#         return max_consecutive


# method3 fastest!
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_consecutive = 0
        curr = 0
        for i in nums:
            if i == 1:
                curr += 1
            else:
                if max_consecutive < curr:
                    max_consecutive = curr
                curr = 0

        if max_consecutive < curr:
            max_consecutive = curr
        return max_consecutive


nums = [1, 1, 0, 1, 1, 1]
test = Solution()
print(test.findMaxConsecutiveOnes(nums))