class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force solution: O(n^2)

        max_area = 0
        
        for idx1 in range(len(heights) - 1):
            for idx2 in range(idx1 + 1, len(heights)):
                x = idx2 - idx1
                y = min(heights[idx2], heights[idx1])
                max_area = max(max_area, x*y)
        
        return max_area
