class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        ans = list()
        x, y, row, column = 0, 0, len(matrix)-1, len(matrix[0])-1

        while x <= row and y <= column:
            i = y
            while i <= column:
                ans.append(matrix[x][i])
                i += 1
            i = x+1
            while i < row:
                ans.append(matrix[i][column])
                i += 1
            i = column
            while i >= y and x != row:
                ans.append(matrix[row][i])
                i -= 1
            i = row-1
            while i > x and y != column:
                ans.append(matrix[i][y])
                i = i-1
            y += 1
            x += 1
            row -= 1
            column -= 1
        return ans


nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

nums1 = [[2, 3]]

nums2 = [[2], [3]]

nums3 = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]
]

test = Solution()
print(test.spiralOrder(nums3))