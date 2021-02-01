'''
414. Third Maximum Number
Problem Link : https://leetcode.com/problems/third-maximum-number/
Runtime: 28 ms
Memory Usage: 14.5 MB
'''
class Solution(object):
    def thirdMax(self, nums):
        if len(nums)<3 or len(set(nums))<3:
            return max(nums)
        else:
            for j in range(0,2):
                t=max(nums)
                for i in range(0,len(nums)):
                    if nums[i]==t:
                        nums[i]=min(nums)
            return max(nums)