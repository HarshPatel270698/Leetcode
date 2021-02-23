'''
524. Longest Word in Dictionary through Deleting
Problem Link : https://leetcode.com/problems/longest-word-in-dictionary-through-deleting
Runtime: 244 ms
Memory Usage: 19.1 MB
'''
class Solution(object):
    def findLongestWord(self, s, d):
        final={}
        count=len(s)
        ts=s
        for i in range(len(d)):
            sub=d[i]
            check=0
            if count>=len(sub):
                for k in range(len(sub)):
                    if sub[k] in ts:
                        check+=1
                        ts=''+ts[ts.index(sub[k])+1:]
                if check==len(sub):
                    final[sub]=len(sub)
            ts=s
        if len(final)==0:
            return ""
        m=max(final.values())
        ans=[]
        for i in final:
            if final[i]==m:
                ans.append(i)
        return sorted(ans)[0]