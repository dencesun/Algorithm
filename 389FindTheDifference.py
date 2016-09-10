class Solution(object):
    def findTheDifference(self, s, t):
    	s = list(s)
    	t = list(t)
        for ch in t:
        	if ch in s:
        		s.remove(ch)
        		continue
        	else:
        		return ch

test = Solution()
print test.findTheDifference('abcd', 'abcde')