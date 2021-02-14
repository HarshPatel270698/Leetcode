'''
1758. Minimum Changes To Make Alternating Binary String
Problem Link : https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
Runtime: 104 ms
Memory Usage: 13.6 MB
'''
class Solution(object):
    def minOperations(self, s):
        if len(s)==1:
            return 0
        countA=0
        countB=0
        for i in range(0,len(s)):
            if i%2==0:
                if int(s[i])==1:
                    countA+=1
            else:
                if int(s[i])==0:
                    countA+=1
        for i in range(0,len(s)):
            if i%2==0:
                if int(s[i])==0:
                    countB+=1
            else:
                if int(s[i])==1:
                    countB+=1
        return min(countA,countB)