def findleaders(nums):
    leader = []

    for i in range(len(nums)):
        is_leader = True

        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                is_leader = False

        if is_leader:
            leader.append(nums[i])

    return leader