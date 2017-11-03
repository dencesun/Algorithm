class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # method1
        # if not matrix or not matrix[0] or target is None:
        #     return False
        # row, column = len(matrix), len(matrix[0])
        # for i in range(row):
        #     if matrix[i][0] <= target <= matrix[i][-1]:
        #         j, k = 0, column-1
        #         while j <= k:
        #             median = int((j+k)/2)
        #             if matrix[i][median] > target:
        #                 k = median-1
        #             elif matrix[i][median] < target:
        #                 j = median+1
        #             else:
        #                 return True
        #         return False
        #
        # return False

        # method2 binary search
        if not matrix or not matrix[0] or target is None:
            return False

        row, column = len(matrix), len(matrix[0])
        top, buttom = 0, row - 1
        while top <= buttom:
            median = int((top + buttom) / 2)
            if matrix[median][0] > target:
                buttom = median - 1
            elif matrix[median][0] < target:
                top = median + 1
            else:
                return True

        left, right = 0, column - 1
        while left <= right:
            median = int((left + right) / 2)
            if matrix[buttom][median] > target:
                right = median - 1
            elif matrix[buttom][median] < target:
                left = median + 1
            else:
                return True
        return False


matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
target = 3

matrix1 = [[]]
test = Solution()
print(test.searchMatrix(matrix, target))
