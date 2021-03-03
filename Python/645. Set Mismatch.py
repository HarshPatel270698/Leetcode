'''
645. Set Mismatch
Problem Link : https://leetcode.com/problems/set-mismatch/
Runtime: 172 ms
Memory Usage: 15.6 MB
'''
class Solution(object):
    def findErrorNums(self, nums):
        s={""}
        ans=[]
        for i in nums:
            if i in s:
                ans.append(i)
            else:
                s.add(i)
        for i in range(1,len(nums)+1):
            if i not in s:
                ans.append(i)
        return ans