class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        val = set()
        while n not in val:
        	val.add(n)
        	newn = 0
        	while n != 0:
        		newn += (n%10)**2
        		n = n/10
        	if newn == 1:
        		return True
        	n = newn
       	return False

test = Solution()
print test.isHappy(19)
