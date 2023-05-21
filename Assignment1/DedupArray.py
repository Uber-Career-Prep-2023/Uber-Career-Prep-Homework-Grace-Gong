"""
Author:Grace Gong 
Technique: two-pointer 
Time Complexity: O(n)
Space Complexity: O(1) 

Time: 40 min
"""
def dedupArray(arr):
    if not arr:
        return []

    writePtr = 1

    for readPtr in range(1, len(arr)):
        if arr[readPtr] != arr[readPtr - 1]:
            arr[writePtr] = arr[readPtr]
            writePtr += 1

    for i in range(writePtr, len(arr)):
        arr[i] = -1

    return arr

test1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
test2 = [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
test3 = [1, 3, 4, 8, 10, 12]

print(dedupArray(test1))  
print(dedupArray(test2))  
print(dedupArray(test3))  
