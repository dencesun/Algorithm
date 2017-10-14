class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0:
            num = nums2
        elif len(nums2)==0:
            num = nums1
        else:
            num = nums1+nums2

        lens = len(num)
        num.sort()
        print num
        if lens%2 == 0:
            return (num[(lens/2)-1]+num[lens/2])/2.0
        return num[lens/2]/1.0
        
test = Solution()
print test.findMedianSortedArrays([1,2],[3])
