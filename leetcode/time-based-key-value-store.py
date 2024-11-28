from collections import defaultdict

import bisect
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # values = self.hashmap[key] # list of [timestamp, value]
        # result = ""
        # for time, val in values:
        #     if time <= timestamp:
        #         result = val
        # return result
        
        values = self.hashmap[key] # list of [timestamp, value]

        result = ""
        left = 0
        right = len(self.hashmap[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                left = mid + 1
                result = values[mid]
            else:
                right = mid - 1
        if result == "":
            return result
        return result[1]


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
print(obj.get("foo", 1))         # return "bar"
print(obj.get("foo", 3))         # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
obj.set("foo", "bar2", 4) # store the key "foo" and value "bar2" along with timestamp = 4.
print(obj.get("foo", 4))         # return "bar2"
print(obj.get("foo", 5))         # return "bar2"

# obj.set("love", "high", 10)
# obj.set("love", "low", 20)
# print(obj.get("love", 5))
# print(obj.get("love", 10))
# print(obj.get("love", 15))
# print(obj.get("love", 20))
# print(obj.get("love", 25))