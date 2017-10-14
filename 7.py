class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
        	return -1*self.reversernum(-x)
        return self.reversernum(x)
    def reversernum(self,num):
    	ch = list(str(num))
    	ch.reverse()
    	return int("".join(ch))

test = Solution()
print test.reversernum(1534236469)
