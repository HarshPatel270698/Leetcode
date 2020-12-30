'''
1374. Generate a String With Characters That Have Odd Counts
Problem Link : https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
Runtime: 4 ms
Memory Usage: 13.3 MB
'''
class Solution(object):
    def generateTheString(self, n):
        a=''
        if n%2==0:
            a+='a'*(n-1)
            a+='b'
            return a
        else:
            a+='a'*n
            return a