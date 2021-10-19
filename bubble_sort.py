def bubble_sort(nums):
    for i in range(0,len(nums)):
        swap_count = 0
        for j in range(0,len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j + 1],nums[j]
                swap_count = swap_count +1
        if swap_count == 0:
            break
    return nums

print(bubble_sort([4,3,1,2]))
