class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left, right = 0, len(height)-1
        maxArea = 0

        while left < right:
            xLength = right - left
            if height[left] < height[right]:
                area = height[left] * xLength
                maxArea = max(maxArea, area)
                left += 1
            else:
                area = height[right] * xLength
                maxArea = max(maxArea, area)
                right -= 1
        return maxArea
