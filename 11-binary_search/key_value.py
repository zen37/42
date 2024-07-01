"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps 
and retrieve the key's value at a certain timestamp.
"""

class TimeMap:

    def __init__(self):
        self.store = {} # dictionary with key, value is list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        
        values = self.store.get(key, []) #if it does not find the key it returns an empty list

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l+r) // 2
            val = values[m]
            if timestamp >= val[1]:
                result = val[0]
                l =  m + 1
            else:
                r = m - 1

        return result
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)