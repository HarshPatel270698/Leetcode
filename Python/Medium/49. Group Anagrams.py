'''
49. Group Anagrams
Problem Link : https://leetcode.com/problems/group-anagrams
Runtime: 1592 ms
Memory Usage: 17.9 MB
'''
class Solution(object):
    def groupAnagrams(self, strs):
        dict={}
        for i in range(0,len(strs)):
            s=sorted(strs[i])
            string=str(s)
            if string in dict.keys():
                x = dict[string]
                x.append(str(strs[i]))
                dict[str(s)]=x
            else:
                s=[strs[i]]
                dict[string]=s
        return dict.values()