'''
1566. Detect Pattern of Length M Repeated K or More Times
Problem Link : https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times
Runtime: 16 ms
Memory Usage: 13.3 MB
'''
class Solution(object):
    def containsPattern(self, arr, m, k):
        if m*k>len(arr):
            return False
        i=0
        while i<=len(arr):
            if len(arr[i:i+m])==m:
                if k*arr[i:m+i] == arr[i:i+m*k]:
                    return True
            i+=1
'''
Runtime: 32 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def containsPattern(self, arr, m, k):
        if m*k>len(arr):
            return False
        i=0
        s2="".join(str(i) for i in arr)
        for j in range(m):
            i=j
            print "i",i,"j nakhya",j
            while i<len(arr):
                if len(arr[i:m+i])==m:
                    print "in"
                    s1="".join(str(i) for i in k*arr[i:m+i])
                    print s1,"in",s2
                    if s1 in s2:
                        return True
                i+=m