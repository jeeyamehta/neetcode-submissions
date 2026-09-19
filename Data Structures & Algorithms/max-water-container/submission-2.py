class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_water = 0

        while l <= r:
            curr = min(heights[l], heights[r]) * (r-l)
            if curr > max_water:
                max_water = curr
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return max_water

        