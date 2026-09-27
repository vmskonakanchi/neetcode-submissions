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

        print(matrix[target_index])

        for i in range(len(matrix[target_index])):
            if matrix[target_index][i] == target:
                return True

        return False
