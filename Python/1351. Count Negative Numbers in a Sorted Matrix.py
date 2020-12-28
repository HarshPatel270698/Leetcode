'''
1351. Count Negative Numbers in a Sorted Matrix
Problem Link : https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
Runtime: 96 ms
Memory Usage: 14.5 MB
'''
class Solution(object):
    def countNegatives(self, grid):
        return str(grid).count('-')
        