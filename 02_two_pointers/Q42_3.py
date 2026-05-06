class Solution:
    def trap(self, height: List[int]) -> int:   # O(n) memory
        n = len(height)
        if n == 0:
            return 0

        maxLeft = [0] * n
        maxRight = [0] * n

        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
            j = n - 1 - i
            maxRight[j] = max(maxRight[j+1], height[j+1])
        
        total = 0
        for i in range(len(height)): 
            potential = min(maxLeft[i], maxRight[i]) - height[i] 
            if potential > 0:
                total += potential
        return total


    def trap2(self, height: List[int]) -> int: # O(1) memory 2pointers

        l, r = 0, len(height) - 1
        maxl = 0
        maxr = 0
        total = 0

        while l < r:
            maxl = max(height[l], maxl)
            maxr = max(height[r], maxr)

            if maxl <= maxr:
                potential = min(maxl, maxr) - height[l]
                if potential > 0:
                    total += potential
                l += 1
            else:
                potential = min(maxl, maxr) - height[r]
                if potential > 0:
                    total += potential
                r -= 1

        return total

  
    def trap(self, height: List[int]) -> int: #OPTIMIZED
        if not height:
            return 0

        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]
        total = 0

        while l < r:
            if maxl <= maxr:
                l += 1
                if maxl < height[l]:
                    maxl = height[l]
                total += maxl - height[l]
            else:
                r -= 1
                if maxr < height[r]:
                    maxr = height[r]
                total += maxr - height[r]
        return total
        
