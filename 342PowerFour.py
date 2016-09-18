class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = list(bin(num))[2:]
        if x.count('1')>1: return False
        x.reverse()
        if x.index('1')%2 == 0: return True
        return False

test = Solution()
print test.isPowerOfFour(16)