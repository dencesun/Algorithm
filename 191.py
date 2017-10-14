# class Solution(object):
#     def hammingWeight(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         tmp = 0
#         while n > 0:
#         	tmp += n&0x1
#         	n = n>>1
#         return tmp
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

test = Solution()
print test.hammingWeight(4294967295)
