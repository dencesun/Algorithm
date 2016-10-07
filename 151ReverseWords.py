class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = filter(None,s.split(' '))
        l.reverse()

        return " ".join(l)

test = Solution()

print test.reverseWords("   a   b  c d   e  ")

