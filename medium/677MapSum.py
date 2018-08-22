class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data=dict()
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.data[key]=val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        res=0
        for i in self.data:
            if i.startswith(prefix):
                res+=self.data[i]
        return res
                


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
