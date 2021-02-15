'''
367. Valid Perfect Square
Problem Link : https://leetcode.com/problems/valid-perfect-square/
Runtime: 16 ms
Memory Usage: 13.4 MB
'''
class Solution(object):
    def isPerfectSquare(self, num):
        return (num**0.5).is_integer()