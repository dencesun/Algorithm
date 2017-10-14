class Solution(object):
    def addDigits(self, num):
    	if num == 0:
    		return 0
    	elif num%9==0:
    		return 9;
    	else:
    		return num%9

test = Solution()
print test.addDigits(14)
