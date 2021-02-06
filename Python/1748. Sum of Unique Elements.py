'''
1748. Sum of Unique Elements
Problem Link : https://leetcode.com/problems/sum-of-unique-elements/
Runtime: 24 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def sumOfUnique(self, nums):
        sum=0
        for i in set(nums):
            if nums.count(i)==1:
                sum+=i
        return sum