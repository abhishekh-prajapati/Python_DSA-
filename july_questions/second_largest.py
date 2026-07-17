def second_largest(nums):
    largest_num = nums[0] 
    second_largest = -1
    for i in nums:
        if i > largest_num:
            second_largest = largest_num
            largest_num = i
        elif i > second_largest and i < largest_num:
            second_largest = i
    return second_largest

     