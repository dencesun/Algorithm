# class Solution:
#     # @param n, an integer
#     # @return an integer
#     def reverseBits(self, n):
#     	x = list(bin(n))[2:]
#     	x.reverse()
#     	return int(''.join(x)+'0'*(32-len(x)), 2)

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    	res = 0
    	for x in range(32):
    		res <<= 1
    		res |= ((n>>x)&1)
    	return res
    	
test = Solution()
print test.reverseBits(1)