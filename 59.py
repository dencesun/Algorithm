class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0]*n for _ in range(n)]
        x, y, row, column = 0, 0, n-1, n-1
        nums = 1
        while x <= row and y <= column:
            i = x
            while i <= column:
                ans[x][i] = nums
                nums += 1
                i = i+1
            i = x+1
            while i <= row:
                ans[i][column] = nums
                nums += 1
                i = i+1
            i = column-1
            while i >= y and y != column:
                ans[row][i] = nums
                nums += 1
                i -= 1
            i = row - 1
            while i > x and x != row:
                ans[i][y] = nums
                nums += 1
                i -= 1

            x += 1
            y += 1
            row -= 1
            column -= 1

        return ans


n = 3
test = Solution()
print(test.generateMatrix(n))
