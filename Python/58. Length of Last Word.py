'''
58. Length of Last Word
Problem Link : https://leetcode.com/problems/length-of-last-word/
Runtime: 20 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        l=s.split()
        if len(l)>0:
            return len(l[-1])
        else:
            return 0