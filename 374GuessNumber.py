# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n, num):
        """
        :type n: int
        :rtype: int
        """
        L, R = 1, n
        while L<=R:
        	mid = (L+R)/2
        	print mid
        	if mid == num:
        		break
        	elif mid < num:
        		L = mid + 1
        	else:
        		R = mid -1

test = Solution()

test.guessNumber(10, 6)