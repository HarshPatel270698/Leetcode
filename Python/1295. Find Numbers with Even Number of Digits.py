'''
1295. Find Numbers with Even Number of Digits
Problem Link : https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
Runtime: 32 ms
Memory Usage: 13.7 MB
'''
class Solution(object):
    def findNumbers(self, nums):
        a=0
        for i in range(len(nums)):
            if len(str(nums[i]))%2==0:
                a+=1
        return a