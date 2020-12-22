'''
1678. Goal Parser Interpretation
Problem Link : https://leetcode.com/problems/goal-parser-interpretation/
Runtime: 12 ms
Memory Usage: 13.6 MB
'''
class Solution(object):
    def interpret(self, command):
        s=command.replace("()","o").replace("(al)","al")
        return s