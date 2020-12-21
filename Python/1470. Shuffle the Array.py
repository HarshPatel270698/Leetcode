'''
1470. Shuffle the Array
Problem Link : https://leetcode.com/problems/shuffle-the-array
Runtime: 48 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def shuffle(self, nums, n):
        a=[]
        for i in range(n):
            a.append(nums[i])
            a.append(nums[i+n])
        return a