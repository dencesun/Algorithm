class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        l = s.split()
        if len(l) == 0: return 0
        return len(l[-1])


test = Solution()
print test.lengthOfLastWord(" ")
