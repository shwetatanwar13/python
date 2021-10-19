def bin_search(nums, item):
    mid = len(nums) / 2
    if nums[mid] == item:
        return mid
    elif nums[mid] > item:
        return bin_search(nums[:mid],item)
    elif nums[mid] < item:
        return bin_search(nums[mid+1:], item)
    elif len(nums)==0:
        return False

print(bin_search([3,5,7,9,12,14], 9))
