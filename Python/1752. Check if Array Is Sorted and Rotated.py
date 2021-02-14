'''
1752. Check if Array Is Sorted and Rotated
Problem Link : https://leetcode.com/problems/check-if-array-is-sorted-and-rotated
Runtime: 28 ms
Memory Usage: 13.4 MB
'''
class Solution(object):
    def check(self, nums):
        sh=sorted(nums)
        nums+=nums
        if str(sh)[1:-1] in str(nums):
            return True