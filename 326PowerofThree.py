class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
        	return False
        while n>1:
        	if n%3 != 0:
        		return False
        	else:
        		n = n/3
        if n == 1:
        	return True
        return False

test = Solution()
print test.isPowerOfThree(8)
print test.isPowerOfThree(9)