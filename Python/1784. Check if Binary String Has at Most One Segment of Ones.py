'''
1784. Check if Binary String Has at Most One Segment of Ones
Problem Link : https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
Runtime: 28 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def checkOnesSegment(self, s):
        count=0
        for i in s:
            if i=="0":
                count+=1
            if count>0 and i=="1":
                return False
        return True