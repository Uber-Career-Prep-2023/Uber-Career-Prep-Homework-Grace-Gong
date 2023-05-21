"""
Author:Grace Gong 
Technique:  variable-size (shrinking/growing) sliding window
Time Complexity: O(n+m) 
Space Complexity: O(n+m) 

Time: 40 min
"""
def shortestSubstring(s, required):
    requiredCount = {}
    for char in required:
        if char in requiredCount:
            requiredCount[char] += 1
        else:
            requiredCount[char] = 1

    windowCount = {}
    left = 0
    right = 0
    formed = 0
    minLen = float('inf')

    while right < len(s):
        if s[right] in windowCount:
            windowCount[s[right]] += 1
        else:
            windowCount[s[right]] = 1

        if s[right] in requiredCount and windowCount[s[right]] <= requiredCount[s[right]]:
            formed += 1

        while formed == len(required):
            minLen = min(minLen, right - left + 1)

            windowCount[s[left]] -= 1
            if s[left] in requiredCount and windowCount[s[left]] < requiredCount[s[left]]:
                formed -= 1

            left += 1

        right += 1

    return minLen if minLen != float('inf') else 0

test1 = ("abracadabra", "abc")
test2 = ("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx")
test3 = ("dog", "god")

print(shortestSubstring(*test1))  
print(shortestSubstring(*test2)) 
print(shortestSubstring(*test3))  
