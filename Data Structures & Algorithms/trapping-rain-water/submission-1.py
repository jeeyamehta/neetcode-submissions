class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r, i = 0, len(height)-1, 0
        trapped = 0

        prefix = [0]*n
        suffix = [0]*n

        prefix[0] = height[0]
        for i in range(1, n):
            prefix[i] = max(prefix[i-1], height[i])


        suffix[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])

        
        for i in range(n):
            trapped += min(prefix[i], suffix[i]) - height[i]
        
        return trapped
            



        
        
        

        