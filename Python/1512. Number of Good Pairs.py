'''
1512. Number of Good Pairs
Problem Link : https://leetcode.com/problems/number-of-good-pairs/
Runtime: 16 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def numIdenticalPairs(self, nums):
        p=0
        for i in range(len(nums)):
            a=nums[i]
            for j in range(i):
                if(a==nums[j]):
                    p+=1
        return p