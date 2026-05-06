class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:  #STILL O(n)

        max_area = 0
        stack = []

        for i, num in enumerate(heights):
            base_index = i
            while stack and num < stack[-1][1]:
                prev_index, prev_num = stack.pop()
                max_area = max(max_area, (i - prev_index) * prev_num) #get max
                base_index = prev_index
            stack.append((base_index, num))

        for i, num in stack:
            max_area = max(max_area, (len(heights) - i) * num)
        return max_area


    def largestRectangleArea2(self, heights: List[int]) -> int: #OPTIMIZED
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n  or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea
