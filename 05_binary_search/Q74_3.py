class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: # O(m * n)
        for i in matrix:
            if target in i:
                return True
        return False 


    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool: # O(m * log n)

        for i in matrix:
            l, r = 0, len(i) - 1
            while l <= r:
                m = (l+r) // 2
                if i[m] > target:
                    r = m - 1
                elif i[m] < target:
                    l = m + 1
                else:
                    return True
        return False 


    def searchMatrix3(self, matrix: List[List[int]], target: int) -> bool: # O(log(m*n)) or O(log(m) + log(n))

        l, r = 0, len(matrix) - 1
        row_index = -1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                row_index = m
                break 

        if row_index == -1:
            return False

        row = matrix[row_index]
        l, r = 0, len(row) - 1

        while l <= r:
            m = (l + r) // 2
            if row[m] > target:
                r = m - 1
            elif row[m] < target:
                l = m + 1
            else:
                return True
        return False
