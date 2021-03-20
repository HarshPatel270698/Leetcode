'''
841. Keys and Rooms
Problem Link : https://leetcode.com/problems/keys-and-rooms/ 
Runtime: 52 ms
Memory Usage: 13.9 MB
'''
class Solution(object):
    def canVisitAllRooms(self, rooms):
        ans=[0]
        v=set()
        while ans:
            t=ans.pop()
            v.add(t)
            for i in rooms[t]:
                if i not in v:
                    ans.append(i)
        return len(v)==len(rooms)