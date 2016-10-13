class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str = s.upper()
        ans = []
        for i in str:
        	if (i >='A' and i <='Z') or (i>='0' and i<='9'):
        		ans.append(i)

        lens = len(ans)
        if lens == 0:
        	return True

        for i in range(lens/2):
        	if ans[i] != ans[lens-1-i]:
        		return False
        return True

test = Solution()
print test.isPalindrome('0b')
