"""Grace Gong 
Technique: forward/backward two-pointer
Time Complexity: O(n+m) 
Space Complexity: O(1) 

Time: 40 min
"""

def backspaces(s, index):
    backspaceCount = 0
    while index >= 0:
        if s[index] == '#':
            backspaceCount += 1
        elif backspaceCount > 0:
            backspaceCount -= 1
        else:
            break
        index -= 1
    return index

def compare(s1, s2):
    i, j = len(s1) - 1, len(s2) - 1

    while i >= 0 or j >= 0:
        i = backspaces(s1, i)
        j = backspaces(s2, j)

        if i < 0 and j < 0:
            return True

        if i < 0 or j < 0 or s1[i] != s2[j]:
            return False

        i -= 1
        j -= 1

    return True

test1 = ("abcde", "abcde")
test2 = ("Uber Career Prep", "u#Uber Careee#r Prep")
test3 = ("abcdef###xyz", "abcw#xyz")
test4 = ("abcdef###xyz", "abcdefxyz###")

print(compare(*test1)) 
print(compare(*test2))  
print(compare(*test3))  
print(compare(*test4))  
