def longestincreasingstreak(nums):
    current_streak = 1
    max_streak = 1

    for i in range(1,len(nums)):
        if nums[i] > nums [i - 1]:
            current_streak += 1
            
            if current_streak > max_streak:
                max_streak = current_streak 
        else:
            current_streak = 1
        
    return max_streak       
            

nums = [1, 3, 2, 4, 5]

print(longestincreasingstreak(nums))