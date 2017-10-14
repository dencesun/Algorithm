class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = list(bin(int(a,2)+int(b,2)))[2:]
        return ''.join(ans)
test = Solution()
print test.addBinary('11', '1')
