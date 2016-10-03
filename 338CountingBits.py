class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = []
        for i in range(num+1):
        	ans.append(bin(i).count('1'))
        return ans
    def test(self, num):
    	print self.countBits(num)

test = Solution()
test.test(5)