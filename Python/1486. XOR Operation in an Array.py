'''
1486. XOR Operation in an Array
Problem Link : https://leetcode.com/problems/xor-operation-in-an-array/
Runtime: 16 ms
Memory Usage: 13.3 MB
'''
class Solution(object):
    def xorOperation(self, n, start):
        s=start
        for i in range(1,n):
            s^=(start+2*i)
        return s