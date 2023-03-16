"""Grace Gong 
Technique: one-directional running computation
Time Complexity: O(n)
Space Complexity: O(n)

Time: 40 min
"""
def zeroSumSubarray(arr):
    n = len(arr)

    sumFreq = {0: 1}
    runningSum = 0
    count = 0

    for num in arr:
        runningSum += num

        if runningSum in sumFreq:
            count += sumFreq[runningSum]

        sumFreq[runningSum] = sumFreq.get(runningSum, 0) + 1

    return count

# Test cases
test1 = [4, 5, 2, -1, -3, -3, 4, 6, -7]
test2 = [1, 8, 7, 3, 11, 9]
test3 = [8, -5, 0, -2, 3, -4]

print(zeroSumSubarray(test1)) 
print(zeroSumSubarray(test2))  
print(zeroSumSubarray(test3)) 
