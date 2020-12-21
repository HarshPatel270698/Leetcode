'''
1480. Running Sum of 1d Array
Problem Link : https://leetcode.com/problems/running-sum-of-1d-array/
Runtime: 24 ms
Memory Usage: 13.4 MB
'''
class Solution(object):
    def runningSum(self, nums):
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        return nums