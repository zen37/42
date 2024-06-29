from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        min_val = matrix[0][0]
        max_val = matrix[-1][-1]

        if target < min_val or target > max_val:
            return False

        l_outer, r_outer = 0, len(matrix) - 1

        while l_outer <= r_outer:
            mid = (l_outer + r_outer) // 2
            row = matrix[mid]

            if target < row[0]:
                r_outer = mid - 1
            elif target > row[-1]:
                l_outer = mid + 1
            else:
                l, r = 0, len(row) - 1
                while l <= r:
                    m = (l + r) // 2
                    if target > row[m]:
                        l = m + 1
                    elif target < row[m]:
                        r = m - 1
                    else:
                        return True
                return False

        return False

class SolutionNeetcode:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) #True
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,800]], 13))#False