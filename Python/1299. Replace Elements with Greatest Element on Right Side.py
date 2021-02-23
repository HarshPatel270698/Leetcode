'''
1299. Replace Elements with Greatest Element on Right Side
Problem Link : https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side
Runtime: 4248 ms
Memory Usage: 14.9 MB
'''
class Solution(object):
    def replaceElements(self, arr):
        for i in range(len(arr)-1):
            arr[i]=max(arr[i+1:])
        arr[-1]=-1
        return arr
'''
Runtime: 100 ms
Memory Usage: 15.6 MB
'''
class Solution(object):
    def replaceElements(self, arr):
        max=-1
        ans=[-1]
        for i in range((len(arr))-1,0,-1):
            if arr[i]>max:
                max=arr[i]
            ans.append(max)
        return ans[::-1]