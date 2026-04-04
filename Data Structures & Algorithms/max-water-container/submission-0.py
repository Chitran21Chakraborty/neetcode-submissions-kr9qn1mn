class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        low = 0
        high = len(heights)-1
        while low<high:
            width = abs(high - low)
            height = min(heights[low], heights[high])
            maximum = max(maximum,width*height)
            if heights[low] < heights[high]:
                low += 1
            else:
                high -=1
        return maximum  

        