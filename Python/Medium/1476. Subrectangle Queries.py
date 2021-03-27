'''
1476. Subrectangle Queries
Problem Link : https://leetcode.com/problems/subrectangle-queries/
Runtime: 188 ms
Memory Usage: 15.7 MB
'''
class SubrectangleQueries(object):

    def __init__(self, rectangle):
        self.s=rectangle        

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                self.s[i][j]=newValue

    def getValue(self, row, col):
        return self.s[row][col]