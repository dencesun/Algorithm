class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return

        left = 0
        right = len(height)-1

        max_area, curr = 0, 0

        while left < right:
            curr = (right-left)*min(height[left], height[right])
            max_area = max(max_area, curr)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


height = [2, 3, 4, 5, 4, 3]
test = Solution()
print(test.maxArea(height))