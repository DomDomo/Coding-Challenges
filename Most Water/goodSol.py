class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxA = 0;
    
        l = 0;
        r = len(height) - 1;
        
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxA = max(maxA, area)            
            
            if height[r] > height[l]:
                l += 1;
            else:
                r -= 1
            
        return maxA
        