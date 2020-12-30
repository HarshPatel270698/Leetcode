'''
905. Sort Array By Parity
Problem Link : https://leetcode.com/problems/sort-array-by-parity/
Runtime: 60 ms
Memory Usage: 14.4 MB
'''
class Solution(object):
    def sortArrayByParity(self, A):
        e=[]
        o=[]
        for i in A:
            if i%2==0:
                e.append(i)
            else:
                o.append(i)
        return e+o