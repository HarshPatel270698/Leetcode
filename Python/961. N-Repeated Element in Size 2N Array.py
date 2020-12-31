'''
961. N-Repeated Element in Size 2N Array
Problem Link : https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
Runtime: 156 ms
Memory Usage: 14.1 MB
'''
class Solution(object):
    def repeatedNTimes(self, A):
        for i in A:
            if len(A)/2==A.count(i):
                return i