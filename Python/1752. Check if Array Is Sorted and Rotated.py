'''
1752. Check if Array Is Sorted and Rotated
Problem Link : https://leetcode.com/problems/check-if-array-is-sorted-and-rotated
Runtime: 24 ms
Memory Usage: 13.4 MB
'''
class Solution(object):
    def check(self, nums):
        sh=sorted(nums)
        s=""
        k=""
        for i in range(0,len(nums)):
            s+=str(nums[i])
        for i in range(0,len(sh)):
            k+=str(sh[i])
        k+=k
        if k.find(s)!=-1:
            return True