class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # time: O(n), space: O(1)

        max_area = 0

        # initialize left and right pointers
        # set up at opposite ends to maximize x distance
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(max_area, area)

            # update the pointer that has the smaller value
            if heights[l] < heights[r]:
                l+=1
            else: 
                r-=1

        return max_area
            
