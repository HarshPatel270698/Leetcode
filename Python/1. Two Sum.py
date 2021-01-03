'''
1. Two Sum
Problem Link : https://leetcode.com/problems/two-sum
Runtime: 32 ms
Memory Usage: 13.3 MB
'''
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]+nums[j]==target:
                    return [i,j]
'''
Runtime: 832 ms
Memory Usage: 13.6 MB
'''
class Solution(object):
    def twoSum(self, nums, target):
        a=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]+nums[j]==target:
                    a.append(i)
        return a
'''
Runtime: 916 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def twoSum(self, nums, target):
        a=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                if nums[i]+nums[j]==target:
                    print nums[i],nums[j]
                    a.append(i)
        return a