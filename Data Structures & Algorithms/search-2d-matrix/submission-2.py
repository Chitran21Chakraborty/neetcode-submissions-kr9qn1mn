class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) #row
        n = len(matrix[0]) #column
        low = 0
        high = m*n-1
        while low<= high:
            mid = (low+high) // 2
            row = mid//n
            col = mid %n
            val = matrix[row][col]

            if target == val:
                return True
            elif target < val:
                high = mid-1
            else:
                low =mid+1
        return False

