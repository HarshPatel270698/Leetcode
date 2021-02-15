'''
643. Maximum Average Subarray I
Problem Link : https://leetcode.com/problems/maximum-average-subarray-i
Runtime: 672 ms
Memory Usage: 16.3 MB
'''
class Solution(object):
    def findMaxAverage(self, nums, k):
        s=sum(nums[:k])
        max=s
        for i in range(1,len(nums)-k+1):
            s=s-nums[i-1]+nums[i+k-1]
            if s>max:
                max=s
        return max/float(k)
'''
Runtime: 732 ms
Memory Usage: 16 MB
'''
class Solution(object):
    def findMaxAverage(self, nums, k):
        if len(nums)==k:
            return sum(nums)/float(k)
        if len(nums)==1:
            return float(nums[0])
        su=sum(nums[:k])
        max=su/float(k)
        for i in range(1,len(nums)-(k)+1):
            s=(su-nums[i-1])+nums[i+k-1]
            ans=s/float(k)
            if ans>max:
                max=ans
            su=s
        return max