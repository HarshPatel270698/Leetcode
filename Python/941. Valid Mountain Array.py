'''
941. Valid Mountain Array
Problem Link : https://leetcode.com/problems/valid-mountain-array/
Runtime: 172 ms
Memory Usage: 14.8 MB
'''
class Solution(object):
    def validMountainArray(self, arr):
        Flag=False
        count=0
        if len(arr)>=3:
            for i in range(1,len(arr)):
                if arr[i-1]<arr[i]:
                    if Flag==False:
                        Flag=True
                        count+=1
                elif arr[i-1]>arr[i]:
                    if arr[i-1]==arr[0]:
                        return False
                    if Flag==True:
                        Flag=False
                        count+=1
                else:
                    return False
            if count==2:
                return True
            else:
                return False
        else:
            False