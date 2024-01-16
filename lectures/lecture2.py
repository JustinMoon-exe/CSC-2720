#  lecture 2
#  write binary search for left and right sorted array target val
#  write binary search for left and right sorted array lowest val

def binarysearch():
    a = [3, 5, 7, 9, 11, 12]  
    target = 5
    low = 0
    high = len(a)-1
    while low <= high:
        mid = low + (high-low)//2
        if target == a[mid]:
            return (mid+1)
        elif a[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return(-1)

def binarysearch2sort():
    a = [4, 5, 6, 9, 10, 0, 1, 2]
    target = 1
    low = 0
    high = len(a)-1
    while low <= high:
        mid = low + (high-low)//2
        if target == a[mid]:
            return (mid+1)
        #  left sorted
        if a[low] <= a[mid]:
            if (target > a[mid]) or (target < a[low]):
                low = mid + 1
            else:
                high = mid - 1
        else:
            if (target < a[mid]) or (target > a[high]):
                high = mid - 1
            else:
                low = mid + 1
    return(-1)

def binarysearch2sortlowval():
    a = [4, 5, 6, 9, 10, 0, 1, 2]
    target = 1
    low = 0
    high = len(a)-1
    while low <= high:
        mid = low + (high-low)//2
        if (a[mid+1] < a[mid]):
            return(mid+1)
        if (a[low] <= a[mid]):
            if a[mid]:
                return(1) #  does not work lol
    return(-1)

print("___________________")


print(binarysearch2sortlowval())

print("___________________")
#syllabus day + linear and binary search