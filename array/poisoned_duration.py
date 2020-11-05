def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    poisonCount = 0
       if len(timeSeries) == 0:
             return poisonCount
        for i in range(len(timeSeries)-1):
            poisonCount+=min(duration, (timeSeries[i+1]-timeSeries[i]))
        poisonCount += duration
        return poisonCount
