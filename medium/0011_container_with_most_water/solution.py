from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        biggest = 0

        while left < right:
            prod = min(heights[left], heights[right]) * (right - left)
            biggest = max(prod, biggest)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return biggest