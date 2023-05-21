# Author: Grace Gong
# Technique: Counting characters
# Time Complexity: O(n)
# Space Complexity: O(n)

def kAnagrams(str1, str2, k):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    count1 = [0] * 26
    count2 = [0] * 26

    for i in range(len(str1)):
        index1 = ord(str1[i]) - ord('a')
        index2 = ord(str2[i]) - ord('a')
        count1[index1] += 1
        count2[index2] += 1

    diff_count = 0
    for i in range(26):
        diff_count += abs(count1[i] - count2[i])

    diff_count = diff_count // 2

    return diff_count <= k

test1 = ("apple", "peach", 1)
test2 = ("apple", "peach", 2)
test3 = ("cat", "dog", 3)
test4 = ("debit curd", "bad credit", 1)
test5 = ("baseball", "basketball", 2)

print(kAnagrams(*test1))  
print(kAnagrams(*test2))  
print(kAnagrams(*test3))  
print(kAnagrams(*test4)) 
print(kAnagrams(*test5))  
