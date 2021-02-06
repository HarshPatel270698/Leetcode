'''
1736. Latest Time by Replacing Hidden Digits
Problem Link : https://leetcode.com/problems/latest-time-by-replacing-hidden-digits
Runtime: 20 ms
Memory Usage: 13.3 MB
'''
class Solution(object):
    def maximumTime(self, time):
        s=str(time)
        if s[0]=='?':
            if s[1]>'3' and s[1]!='?':
                s= s.replace('?','1',1)
            else:
                s= s.replace('?','2',1)
        if s[1]=='?':
            if s[0]=='0' or s[0]=='1':
                s= s.replace('?','9',1)    
            else:
                s= s.replace('?','3',1)
        if s[3]=='?':
            s= s.replace('?','5',1)
        if s[4]=='?':
            s= s.replace('?','9',1)
        return s