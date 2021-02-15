'''
66. Plus One
Problem Link : https://leetcode.com/problems/plus-one
Runtime: 16 ms
Memory Usage: 13.4 MB
'''
class Solution(object):
    def plusOne(self, digits):
        s=""
        for i in digits:
            s+=str(i)
        i=int(s)
        s=str(i+1)
        ans=[]
        for i in s:
            ans.append(i)
        return ans
