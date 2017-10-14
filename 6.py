class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s)<numRows:
        	return s

        tmp = ['' for i in range(numRows)]
        step = 1
        row = 0
        for ch in s:
        	if row == 0:
        		step = 1
        	if row == numRows-1:
        		step = -1
        	tmp[row] += ch
        	row += step
        return "".join(tmp)

test = Solution()
print test.convert("PAYPALISHIRING", 3)

