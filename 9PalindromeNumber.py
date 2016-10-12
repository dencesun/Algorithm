class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        numstr = str(x)
        lens = len(numstr)
        for i in range(lens/2):
            if numstr[i] != numstr[lens-1-i]:
                return False
        return True
        