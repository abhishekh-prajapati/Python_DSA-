def isAnagram(s , t):
    if len(s) != len(t):
        return False
    
    count = {}

    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in t:
        if i not in count:
            return False
        
        count[i] -= 1

    for value in count.values():
        if value != 0:
            return False
    return True

print(isAnagram("anagram", "nagaram")) 