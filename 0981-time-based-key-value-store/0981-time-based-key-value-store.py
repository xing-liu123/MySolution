class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.map:
            self.map[key] = []

        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""

        index = bisect.bisect_right(self.map[key], (timestamp, chr(127)))

        if index == 0:
            return ""
            
        return self.map[key][index - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)