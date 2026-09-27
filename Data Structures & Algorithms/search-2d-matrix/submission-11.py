class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m , n = len(matrix), len(matrix[0])
        t , b = 0, len(matrix) - 1
        row = 0
        while t <= b:
            row = (t + b) // 2
            if target > matrix[row][-1]:
                t = row + 1
            elif target < matrix[row][0]:
                b = row - 1
            else:
                break

        if not (t <= b):
            return False
        
        result_m = matrix[row]

        l , r = 0 , len(result_m) - 1
        while l <= r:
            mid = (r + l) // 2
            curr = result_m[mid]
            if target > curr:
                l = mid + 1
            elif target < curr:
                r = mid - 1
            else:
                return True

        return False
