class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # method1
        # if not matrix:
        #     return
        #
        # row, column = len(matrix), len(matrix[0])
        # rowindex, colindex = list([False])*row, list([False])*column
        #
        # for i in range(row):
        #     for j in range(column):
        #         if matrix[i][j] == 0:
        #             rowindex[i] = True
        #             colindex[j] = True
        #
        # for i in range(row):
        #     if rowindex[i]:
        #         for j in range(column)
        #             matrix[i][j] = 0
        # for i in range(column):
        #     if colindex[i]:
        #         for j in range(row):
        #             matrix[j][i] = 0

        # method2

        # if not matrix:
        #     return
        #
        # row, column = len(matrix), len(matrix[0])
        # rowindex, colindex = False, False
        #
        # for i in range(row):
        #     if matrix[i][0] == 0:
        #         rowindex = True
        #         break
        # for i in range(column):
        #     if matrix[0][i] == 0:
        #         colindex = True
        #         break
        #
        # for i in range(1, row):
        #     for j in range(1, column):
        #         if matrix[i][j] == 0:
        #             matrix[i][0] = 0
        #             matrix[0][j] = 0
        #
        # for i in range(1, row):
        #     for j in range(1, column):
        #         if matrix[i][0] == 0 or matrix[0][j] == 0:
        #             matrix[i][j] = 0
        #
        # if rowindex:
        #     for i in range(row):
        #         matrix[i][0] = 0
        # if colindex:
        #     for i in range(column):
        #         matrix[0][i] = 0

        # method3

        if not matrix:
            return matrix

        row, column = len(matrix), len(matrix[0])
        flag = False #记录第一列时候有0

        for i in range(row):
            if matrix[i][0] == 0:
                flag = True
            for j in range(1, column):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        i = row-1
        while i >= 0:
            for j in range(1, column):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag:
                matrix[i][0] = 0
            i -= 1

matrix1 = [[1, 2, 3],
          [4, 0, 6],
          [0, 9, 0]]

matrix2 = [[0, 0, 1],
           [1, 2, 3]]

test = Solution()
test.setZeroes(matrix2)
print(matrix2)