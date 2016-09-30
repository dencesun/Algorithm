class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # ans = list(str(self.getans(n)))
# timeout
    #     ans = self.getans(n)
    #     count = 0
    #     remainder = 0
    #     while remainder == 0:
    #     	remainder = ans%10
    #     	if remainder == 0:
    #     		count +=1
    #     	ans /=10

    #     return count
    # def getans(self, n):
    # 	if n>=1:
    #     	return n*self.getans(n-1)
    #     return 1
    	count = 0
    	while n:
    		n //= 5
    		count += n
    	return count
test = Solution()
print test.trailingZeroes(25)
