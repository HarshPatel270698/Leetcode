'''
1684. Count the Number of Consistent Strings
Problem Link : https://leetcode.com/problems/count-the-number-of-consistent-strings/
Runtime: 228 ms
Memory Usage: 16.2 MB
'''
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        a=len(words)
        for i in range(len(words)):
            for j in range(len(words[i])):
                if (words[i][j] not in allowed):
                    a-=1
                    break
        return a