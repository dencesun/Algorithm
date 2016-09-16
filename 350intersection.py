class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        tmp = []
        for x in nums1:
        	if x in nums2:
        		tmp.append(x)
        		nums2.remove(x)
       	return tmp

test = Solution()
print test.intersect([1,2,2,1], [2,2])
print test.intersect([1,2,2,1], [])
