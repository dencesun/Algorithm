class Solution(object):
    def isUgly(self, n):
        """
        :type num: int
        :rtype: bool
        """
        tmp = set([2,3,5])
        flag = 0
        if n <= 0:
        	return False
        if n == 1:
        	return True
        while n>1:
        	if n%2==0:
        		n = n/2
        	elif n%3==0:
        		n = n/3
        	elif n%5==0:
        		n/=5
        	else:
        		return False
        return False

test = Solution()
print test.isUgly(31)
