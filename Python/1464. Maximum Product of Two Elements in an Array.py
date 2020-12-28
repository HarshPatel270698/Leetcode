'''
1464. Maximum Product of Two Elements in an Array
Problem Link : https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array
Runtime: 28 ms
Memory Usage: 13.7 MB
'''
class Solution(object):
    def maxProduct(self, nums):
        nums.sort(reverse=True)
        a=(nums[0]-1)*(nums[1]-1)
        return a