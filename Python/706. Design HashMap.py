'''
706. Design HashMap
Problem Link : https://leetcode.com/problems/design-hashmap
Runtime: 168 ms
Memory Usage: 16.3 MB
'''
class MyHashMap(object):
    def __init__(self):
        self.dict={}
        
    def put(self, key, value):
        self.dict[key]=value        

    def get(self, key):
        return self.dict.get(key,-1)       

    def remove(self, key):
        self.dict[key]=-1
'''
Runtime: 496 ms
Memory Usage: 16.1 MB
'''
class MyHashMap(object):

    def __init__(self):
        self.dict={}
        """
        Initialize your data structure here.
        """
        

    def put(self, key, value):
        self.dict[key]=value
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        

    def get(self, key):
        if key in self.dict.keys():
            return self.dict[key]
        return -1
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        

    def remove(self, key):
        if key in self.dict.keys():
            self.dict.pop(key)
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)