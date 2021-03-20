'''
535. Encode and Decode TinyURL
Problem Link : https://leetcode.com/problems/encode-and-decode-tinyurl/
Runtime: 16 ms
Memory Usage: 13.6 MB
'''
class Codec:
    def __init__(self):
        self.abc=[]
        
    def encode(self, longUrl):
        self.abc.append(longUrl)
        return 'http://tinyurl.com/'+str(len(self.abc))
        

    def decode(self, shortUrl):
        return self.abc[int(shortUrl.split('/')[-1])-1]