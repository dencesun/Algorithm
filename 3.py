class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = []
        for i in s:
        	if i not in ans:
        		ans.append(i)
        return len(ans)

test = Solution()
print test.lengthOfLongestSubstring('pwwkew')
