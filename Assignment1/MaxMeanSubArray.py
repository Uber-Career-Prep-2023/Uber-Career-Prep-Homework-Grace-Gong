"""
Author:Grace Gong 
Technique: fixed-size sliding window 
Time Complexity: O(n) 
Space Complexity: O(1) 

Time: 40 min
"""
def maxMeanSubarray(arr, k):
    n = len(arr)
    if n < k:
        return None

    windowSum = sum(arr[:k])
    max_sum = windowSum

    for i in range(n - k):
        windowSum = windowSum - arr[i] + arr[i + k]
        max_sum = max(max_sum, windowSum)

    return max_sum / k

test1 = ([4, 5, -3, 2, 6, 1], 2)
test2 = ([4, 5, -3, 2, 6, 1], 3)
test3 = ([1, 1, 1, 1, -1, -1, 2, -1, -1], 3)
test4 = ([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5)

print(maxMeanSubarray(*test1))  
print(maxMeanSubarray(*test2))  
print(maxMeanSubarray(*test3))  
print(maxMeanSubarray(*test4)) 

