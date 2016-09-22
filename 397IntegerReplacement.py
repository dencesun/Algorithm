class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 0
        if n&1==0: return self.integerReplacement(n/2)+1
        else: return min(self.integerReplacement(n+1), self.integerReplacement(n-1))+1

    def test(self, num):
    	print self.integerReplacement(num)

test = Solution()
test.test(1234)
