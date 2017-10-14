class Solution(object):
    def titleToNumber(self, s):
    	sum = 0
    	n = len(s)
    	for i in range(n):
    		sum = sum*26+ord(s[i])-ord('A')+1
    	return sum

test = Solution()
print test.titleToNumber('AB')
