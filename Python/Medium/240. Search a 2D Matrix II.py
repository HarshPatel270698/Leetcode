'''
240. Search a 2D Matrix II
Problem Link : https://leetcode.com/problems/search-a-2d-matrix-ii
Runtime: 132 ms
Memory Usage: 19.6 MB
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        end=len(matrix)
        for i in range(len(matrix[0])):
            if matrix[0][i]<=target<=matrix[end-1][i]:
                for j in range(end):
                    if target==matrix[j][i]:
                        return True