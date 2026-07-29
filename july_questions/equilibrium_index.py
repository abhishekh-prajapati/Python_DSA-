def equilibrium(nums):
    
    for i in range(len(nums)):
        s1 = 0
        s2 = 0
        for j in range(i):
            s1 += nums[j]

        for j in range(i + 1, len(nums)):
            s2+= nums[j]

        if s1 == s2:
            return i

    return -1

nums = [1, 7, 3, 6, 5, 6]
print(equilibrium(nums))