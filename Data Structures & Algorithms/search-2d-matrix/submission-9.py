class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        target_index = -1

        for i in range(m):
            max_of_row = matrix[i][n-1]

            if target <= max_of_row:
                target_index = i
                break

        if target_index == -1:
            return False
            
        result_m = matrix[target_index]

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
