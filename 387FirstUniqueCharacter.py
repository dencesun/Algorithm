import collections

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
       	if len(s) == 0: return -1
       	counts = collections.Counter(s)
       	for ch in s:
       		if counts[ch] == 1:
       			return s.index(ch)
       	return -1

test = Solution()

print test.firstUniqChar('loveleetcode')
print test.firstUniqChar('leetcode')
print test.firstUniqChar('cc')
print test.firstUniqChar("")
