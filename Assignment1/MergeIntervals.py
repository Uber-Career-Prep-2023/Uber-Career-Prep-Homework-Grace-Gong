"""
Author:Grace Gong 
Technique: sorting
Time Complexity: O(nlogn)
Space Complexity: O(n)

Time: 40 min
"""
def sortKey(interval):
    return interval[0]

def mergeIntervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=sortKey)
    mergedIntervals = [intervals[0]]

    for interval in intervals[1:]:
        lastInterval = mergedIntervals[-1]

        if lastInterval[1] >= interval[0]:
            mergedIntervals[-1] = (lastInterval[0], max(lastInterval[1], interval[1]))
        else:
            mergedIntervals.append(interval)

    return mergedIntervals

test1 = [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
test2 = [(5, 8), (6, 10), (2, 4), (3, 6)]
test3 = [(10, 12), (5, 6), (7, 9), (1, 3)]

print(mergeIntervals(test1))  
print(mergeIntervals(test2))  
print(mergeIntervals(test3))  

