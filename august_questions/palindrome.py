def palindrome (data):
    left = 0
    right = len(data) -1
    for i in range(len(data)):
        if data[left] != data[right]:
            return False
        left += 1
        right -= 1
    return True
