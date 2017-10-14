class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        higher = len(numbers)-1
        ans = []
        while low<higher:
            if numbers[low] + numbers[higher] < target:
                low += 1
            elif numbers[low] + numbers[higher]>target:
                higher -= 1
            else:
                ans.append(low+1)
                ans.append(higher+1)
                return ans
        return ans


nums = [0, 0, 3, 4]
test = Solution()
print(test.twoSum(nums, 0))
