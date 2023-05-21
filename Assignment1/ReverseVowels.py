"""
Author:Grace Gong 
Technique:  forward/backward two-pointer
Time Complexity:  O(n) 
Space Complexity: O(n) 

Time: 40 min
"""
def isVowel(ch):
    return ch.lower() in 'aeiou'

def reverseVowels(s):
    s = list(s)
    i, j = 0, len(s) - 1

    while i < j:
        if not isVowel(s[i]):
            i += 1
        elif not isVowel(s[j]):
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    return ''.join(s)

test1 = "Uber Career Prep"
test2 = "xyz"
test3 = "flamingo"

print(reverseVowels(test1))  
print(reverseVowels(test2)) 
print(reverseVowels(test3))  
