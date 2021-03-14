'''
167. Two Sum II - Input array is sorted
Problem Link : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Runtime: 44 ms
Memory Usage: 13.6 MB
'''
class Solution(object):
    def twoSum(self, numbers, target):
        i,j=0,len(numbers)-1
        while i!=j:
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j]>target:
                j-=1
            else:
                i+=1