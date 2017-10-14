class Solution(object):
    def intersection(self, nums1, nums2):
        tmp = list()
        if len(nums1) == 0:
            return tmp

        for num in nums2:
            if num in nums1:
                if num not in tmp:
                    tmp.append(num)

        return tmp

test = Solution()
print test.intersection([1,2], [2,1])
