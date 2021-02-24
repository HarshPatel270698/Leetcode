'''
74. Search a 2D Matrix
Problem Link : https://leetcode.com/problems/search-a-2d-matrix 
Runtime: 36 ms
Memory Usage: 13.9 MB
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        end=len(matrix)
        for i in range(len(matrix)):
            if matrix[i][0]>=target or i+1==len(matrix):
                for j in range(len(matrix[0])):
                    if target==matrix[i][j] or target==matrix[i-1][j]:
                        return True