class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        while left <= right :
            mid1 = (left +right)//2
            if matrix[mid1][0]<= target and matrix[mid1][-1]>= target:
                break
            elif matrix[mid1][0]< target :
                left = mid1 +1
            else :
                right = mid1 -1
        left2 = 0
        right2 = len(matrix[mid1]) -1
        while left2 <= right2:
            mid2 = (left2+right2)//2
            if matrix[mid1][mid2] == target:
                return True 
            elif matrix [mid1][mid2] < target:
                left2 = mid2 +1
            else :
                right2 = mid2 - 1
        return False 
