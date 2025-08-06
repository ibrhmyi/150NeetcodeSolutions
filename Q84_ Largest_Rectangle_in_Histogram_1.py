class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:  

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
