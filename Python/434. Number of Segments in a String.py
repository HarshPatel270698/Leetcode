'''
434. Number of Segments in a String
Problem Link : https://leetcode.com/problems/number-of-segments-in-a-string
Runtime: 16 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def countSegments(self, s):
        word=0
        count=True
        for i in range(0,len(s)):
            if s[i]!=" " and count==True:
                word+=1
                count=False
            if s[i]==" ":
                count=True
        return word