'''
1773. Count Items Matching a Rule
Problem Link : 
Runtime: 196 ms
Memory Usage: 21.1 MB
'''
class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        count=0
        if ruleKey=="type":
            for i in range(len(items)):
                if items[i][0]==ruleValue:
                    count+=1
            return count
        if ruleKey=="color":
            for i in range(len(items)):
                if items[i][1]==ruleValue:
                    count+=1
            return count
        if ruleKey=="name":
            for i in range(len(items)):
                if items[i][2]==ruleValue:
                    count+=1
            return count