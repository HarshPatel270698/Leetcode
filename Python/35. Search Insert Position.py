'''
35. Search Insert Position
Problem Link : https://leetcode.com/problems/search-insert-position
Runtime: 36 ms
Memory Usage: 14.2 MB
'''
class Solution(object):
    def searchInsert(self, nums, target):
        if target>nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            if target==nums[i] or nums[i]>target:
                return i