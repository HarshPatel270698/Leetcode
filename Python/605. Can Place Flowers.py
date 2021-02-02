'''
605. Can Place Flowers
Problem Link : https://leetcode.com/problems/can-place-flowers/
Runtime: 144 ms
Memory Usage: 14.2 MB
'''
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        meet=0
        if len(flowerbed)>2:
            if flowerbed[0]==0 and flowerbed[1]==0:
                flowerbed[0]=1
                meet+=1
            for i in range(1,len(flowerbed)-1):
                if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    meet+=1
            if flowerbed[len(flowerbed)-2]==0 and flowerbed[len(flowerbed)-1]==0:
                meet+=1            
        elif len(flowerbed)==2 and flowerbed[0]==0 and flowerbed[1]==0:
            meet+=1
        elif len(flowerbed)==1 and flowerbed[0]==0:
            meet+=1
        return meet>=n