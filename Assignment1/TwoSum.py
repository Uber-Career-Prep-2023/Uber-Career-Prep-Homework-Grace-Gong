"""
Author:Grace Gong 
Technique: hashing
Time Complexity: O(n)
Space Complexity: O(n)

Time: 40 min
"""
def twoSum(arr, k):
    # Count the frequency of each number
    numFreq = {}
    for num in arr:
        numFreq[num] = numFreq.get(num, 0) + 1

    count = 0
    for num in numFreq:
        complement = k - num
        if complement in numFreq:
            if complement == num:
                count += (numFreq[num] * (numFreq[num] - 1)) // 2
            else:
                count += numFreq[num] * numFreq[complement]
                del numFreq[complement]

    return count

test1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
test2 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]

print(twoSum(test1, 10))  
print(twoSum(test1, 9))   
print(twoSum(test2, 6))  
print(twoSum(test2, 1))   
