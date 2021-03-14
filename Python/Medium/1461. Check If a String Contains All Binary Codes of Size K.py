'''
1461. Check If a String Contains All Binary Codes of Size K
Problem Link : https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k 
Runtime: 264 ms
Memory Usage: 44.7 MB
'''
class Solution(object):
    def hasAllCodes(self, s, k):
        ans={s[i:i+k] for i in range(len(s)-k+1)} 
        return len(ans)==2**k
'''
Runtime: 308 ms
Memory Usage: 44.9 MB
'''
class Solution(object):
    def hasAllCodes(self, s, k):
        ans=set()
        for i in range(len(s)-k+1):
            ans.add(s[i:i+k])
            if len(ans)==2**k:
                return True