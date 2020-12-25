'''
1662. Check If Two String Arrays are Equivalent
Problem Link : https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
Runtime: 16 ms
Memory Usage: 13.6 MB
'''
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        if ''.join(word1)==''.join(word2):
            return True