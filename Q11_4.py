class Solution: 
    def maxArea(self, height: List[int]) -> int: #BRUTEFORCE
        mymax  = 0
        for l in range(len(height)):
            for r in range(l +1, len(height)):
                area = min(height[l], height[r]) * (r - l)
                mymax = max(res,area)
        return mymax


    def maxArea2(self, height: List[int]) -> int: #2pointers 
        mymax  = 0
        l, r = 0, len(height) -1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            mymax = max(mymax,area)
            if height[l] < height[r]:
                l += 1
            else:
                r -=1
        return mymax

  
    def maxArea3(self, height: List[int]) -> int: #2pointers SEMIOPTIMIZED
        l = 0
        r = len(height)-1
        maxArea = 0

        while l < r:
            area = min(height[l],height[r])*(r-l)
            maxArea = max(maxArea,area)

            if height[l] < height[r]:
                l = l + 1
                while l < r and height[l] <= height[l-1]:
                    l += 1
            else:
                r = r - 1
                while l < r and height[r] <= height[r+1]:
                    r -= 1

        return maxArea



    def maxArea(self, height: List[int]) -> int: #2pointers OPTIMIZED
        l = 0
        r = len(height)-1
        maxArea = 0

        while l < r:
            area = min(height[l],height[r])*(r-l)
            if maxArea < area:
                maxArea = area

            if height[l] < height[r]:
                ll = l + 1
                while ll < r and height[ll] <= height[l]:
                    ll += 1
                l = ll
            else:
                rr = r - 1
                while l < rr and height[rr] <= height[r]:
                    rr -= 1
                r = rr
                
        return maxArea
        
