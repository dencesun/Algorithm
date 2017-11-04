
MAX_VALUE = 2147483647
MIN_VALUE = -2147483648

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        flag = 1
        str = str.strip()
        if str[0] == '-':
            flag = -1
            str = str[1:]
        elif str[0] == '+':
            flag = 1
            str = str[1:]

        num = 0
        for c in str:
            if c>='0' and c<='9':
                num = num*10 + ord(c) - ord('0')
            else:
                break

        num = num*flag
        num = num if num <= MAX_VALUE else MAX_VALUE
        num = num if num >= MIN_VALUE else MIN_VALUE

        return num


str = '1'
test = Solution()
print(test.myAtoi(str))