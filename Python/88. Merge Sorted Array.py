'''
88. Merge Sorted Array
Problem Link : https://leetcode.com/problems/merge-sorted-array
Runtime: 16 ms
Memory Usage: 13.3 MB
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        c=len(nums1)
        while c>m:
            if 0 in nums1:
                nums1.remove(0)
            c-=1
        for i in range(0,len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()