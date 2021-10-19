def selection_sort(nums):
    for i in range(0,len(nums)):
        max_number = nums[0]
        index = 0
        for j in range(0,len(nums)-i):
            if nums[j] > max_number:
                max_number = nums[j]
                index = j
        print(nums)
        nums[len(nums)-1-i],nums[index] = nums[index],nums[len(nums)-1-i]

    return nums

print(selection_sort([11, 7, 12, 14, 19, 1, 6, 18, 8, 20]))
