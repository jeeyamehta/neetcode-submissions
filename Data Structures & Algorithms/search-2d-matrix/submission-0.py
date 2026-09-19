class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, last = 0, len(matrix)-1
        col, end = 0, len(matrix[0]) -1

        while row <= len(matrix)-1:
            if matrix[row][-1] < target:
                row += 1
            else:
                while col <= len(matrix[0]) -1:
                    if matrix[row][col] == target:
                        return True
                    elif matrix[row][col] < target:
                        col += 1
                    else:
                        return False
        return False


            