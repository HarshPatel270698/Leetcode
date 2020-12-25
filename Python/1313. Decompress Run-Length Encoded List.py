'''
1313. Decompress Run-Length Encoded List
Problem Link : https://leetcode.com/problems/decompress-run-length-encoded-list/
Runtime: 64 ms
Memory Usage: 13.6 MB
'''
class Solution(object):
    def decompressRLElist(self, nums):
        a=[]
        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                a.append(nums[i+1])
        return a