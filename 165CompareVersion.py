class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        if len(v1)<len(v2):
        	v1.extend([0]*(len(v2)-len(v1)))
        else:
        	v2.extend([0]*(len(v1)-len(v2)))
        return cmp(v1,v2)


test = Solution()
print test.compareVersion('0.01.0.1', '0.0.1')