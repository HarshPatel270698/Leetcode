'''
1346. Check If N and Its Double Exist
Problem Link : https://leetcode.com/problems/check-if-n-and-its-double-exist
Runtime: 32 ms
Memory Usage: 13.6 MB
'''
class Solution(object):
    def checkIfExist(self, arr):
        l=set(arr)
        if arr.count(0)>1:
            return True
        if len(l)==1:
            if 0 in l:
                return True
            else:
                return False
        for i in l:
            if i%2==0 and i!=0:
                if i/2 in l or i*2 in l:
                    print i
                    return True