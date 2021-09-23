class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxA = 0;
        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height):
                if i != j:
                    h = min(h1, h2)
                    w = j - i
                    area = h * w
                    maxA = max(maxA, area)
        return maxA