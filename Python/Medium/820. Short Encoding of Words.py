'''
820. Short Encoding of Words
Problem Link : https://leetcode.com/problems/short-encoding-of-words
Runtime: 308 ms
Memory Usage: 14 MB
'''
class Solution(object):
    def minimumLengthEncoding(self, words):
        s=""
        words.sort(key=len, reverse=True) #sorted words in reversed order by length to avoid test case like ["me","meme"]
        for i in words: #go through each words
            if i+"#" not in s: #check if word# is not in our string
                s+=i+"#" #if it is not then append word#
        return len(s) #return length