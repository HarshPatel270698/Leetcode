'''
268. Missing Number
Problem Link : https://leetcode.com/problems/missing-number/
Runtime: 96 ms
Memory Usage: 14.8 MB
'''
class Solution(object):
    def missingNumber(self, nums):
        return len(nums)*(len(nums)+1)/2-sum(nums)
'''
Runtime: 2064 ms
Memory Usage: 14.8 MB
'''
class Solution(object):
    def missingNumber(self, nums):
        for i in range(len(nums)+1):
            if i not in nums:
                return i