from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # solution1
        # if not nums:
        #     return []
        # n = int(len(nums)/3)+1
        # nums = Counter(nums)
        # ans = list()
        # for k, v in nums.items():
        #     if v >= n:
        #         ans.append(k)
        #
        # return ans


        # solution2
        if not nums:
            return []

        candidate1, candidate2, count1, count2 = 0, 0, 0, 0
        ans = list()

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        if count1 > len(nums) / 3:
            ans.append(candidate1)
        if count2 > len(nums) / 3:
            ans.append(candidate2)

        return ans


nums = [1, 1, 1, 1, 2, 2, 3, 3]
test = Solution()
print(test.majorityElement(nums))
