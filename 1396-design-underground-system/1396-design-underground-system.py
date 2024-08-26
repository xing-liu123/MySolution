class UndergroundSystem:

    def __init__(self):
        self.times = {}
        self.passengers = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passengers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.passengers[id]
        
        if (startStation, stationName) not in self.times:
            self.times[(startStation, stationName)] = [0, 0]

        self.times[(startStation, stationName)][0] += (t - startTime) 
        self.times[(startStation, stationName)][1] += 1
        del self.passengers[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if not (startStation, endStation) in self.times:
            return 0
        
        return self.times[(startStation, endStation)][0] / self.times[(startStation, endStation)][1]



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)