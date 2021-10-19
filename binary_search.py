def binary_search(l, item):
    low = 0
    high = len(l)-1
    mid = (low + high) / 2
    found = False
    while low <= high and not found:
        if l[mid] > item:
            high = mid-1
        elif l[mid] < item:
            low = mid +1
        else:
            found = True
            break
        mid =  (low + high) / 2
        print(mid)
    print("Found at "+ str(mid) if found else "Not found at " + str(mid))

binary_search([3,5,7,9,12,14], 15)
