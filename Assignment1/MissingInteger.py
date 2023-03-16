"""Grace Gong 
Technique: binary search variation 
Time Complexity: O(logn)
Space Complexity: O(1) 

Time: 40 min
"""
def missingInteger(arr, n):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            right = mid - 1

    return left + 1

test1 = ([1, 2, 3, 4, 6, 7], 7)
test2 = ([1], 2)
test3 = ([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12)

print(missingInteger(*test1))  
print(missingInteger(*test2))  
print(missingInteger(*test3)) 
