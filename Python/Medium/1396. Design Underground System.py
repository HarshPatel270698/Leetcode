'''
1396. Design Underground System
Problem Link : https://leetcode.com/problems/design-underground-system/
Runtime: 236 ms, faster than 51.06% of Python online submissions for Design Underground System.
Memory Usage: 23.9 MB, less than 100.00% of Python online submissions for Design Underground System.
'''
class UndergroundSystem(object):

    def __init__(self):
        self.normal=[]
        self.docc={}
        self.dtotal={}

    def checkIn(self, id, stationName, t):
        self.normal.append([id,stationName,t])        

    def checkOut(self, id, stationName, t):
        for i in range(len(self.normal)):
            if self.normal[i][0]==id:
                s=self.normal[i][1]+stationName
                if s in self.docc:
                    up=self.docc[s]
                    up+=1
                    self.docc[s]=up
                    total=self.dtotal[s]
                    total+=t-self.normal[i][-1]
                    self.dtotal[s]=total
                else:
                    self.docc[s]=1
                    self.dtotal[s]=t-self.normal[i][-1] 
                self.normal.pop(i)
                return

    def getAverageTime(self, startStation, endStation):
        s=startStation+endStation
        return float((self.dtotal[s])*1.0/(self.docc[s]))