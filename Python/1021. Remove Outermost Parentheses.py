'''
1021. Remove Outermost Parentheses
Problem Link : https://leetcode.com/problems/remove-outermost-parentheses
Runtime: 28 ms
Memory Usage: 13.8 MB
'''
class Solution(object):
    def removeOuterParentheses(self, S):
        c=0
        tans=''
        ans=''
        for i in range(len(S)):
            if S[i] == '(':
                c+=1
                tans+=S[i]
            else:
                c-=1
                tans+=S[i]
            if c==0:
                ans+=tans[1:len(tans)-1]
                tans=''
        return ans