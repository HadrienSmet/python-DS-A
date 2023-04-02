def merge_sort(list):
    '''
    Strategy of divide and conquer

    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Runs in overall O(kn log n) time
    '''

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    last = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    Takes overall O(k log n) time. Runs in logarithmic time
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the proces
    Returns a new merged list
    Runs in overall O(n)
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
        
    while i < len(left):
        l.append(left[i])
        i+=1
    
    while j < len(right):
        l.append(right[j])
        j+=1

    return l

alist = [40, 13, 67, 54, 96, 8, 24, 77]
new_list = merge_sort(alist)
print(new_list)

def verify_sorted(list):
    n = len(list)

    if n == 0 or n==1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])
