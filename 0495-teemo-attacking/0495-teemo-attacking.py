class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        currTime = timeSeries[0]

        for i in timeSeries[1:]:
            if (currTime + duration < i):
                total += duration    
            else:
                total += i - currTime

            currTime = i
        return total + duration

# intuition iterate timeseries, starting from 0 to largest number/last item in list
# keep a duration counter
# when hit, then decrease each iteration, unless hit again
# another variable to total up the durations
# then return total and remaining duration
# and remember the duration is inclusive therefore totalling up should be underneath duration refresh
# this is for complete simulation

# for more efficient approach, try to only iterate through number of items
# normal case, where the duration expires before the next hit, just add the duration to total
# edge case where the duration will bleed into the next hit time frame, add the difference between the 2 time frame
# for end, there will always be an hit at the end, without pausing so add the duration
