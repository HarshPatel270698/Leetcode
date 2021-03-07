'''
1534. Count Good Triplets
Problem Link : https://leetcode.com/problems/count-good-triplets/
Runtime: 320 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        l,count=len(arr),0
        for i in range(l):
            for j in range(i+1,l):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j+1,l):
                        if abs(arr[j] - arr[k]) <= b:
                            if abs(arr[i] - arr[k]) <= c:
                                count+=1
        return count
'''
Runtime: 540 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        l,count=len(arr),0
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count+=1
        return count