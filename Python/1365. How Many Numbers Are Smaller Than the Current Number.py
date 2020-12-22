'''
1365. How Many Numbers Are Smaller Than the Current Number
Problem Link : https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number
Runtime: 376 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        a=0
        c=[]
        for i in range(len(nums)):
            t=nums[i]
            for j in range(len(nums)):
                if (t > nums[j]):
                    a+=1
            c.append(a)
            a=0
        return c