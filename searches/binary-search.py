
def iterative_binary_search(list, target):
    """
    Binary search, is very effective and efficient for large arrays. As the size of the array doubles
    Binary search only needs one more action or step for each double of the array size.

    Args:
        list (_type_): an array of items. any data type
        target (_type_): a value to locate within the list. type depends on the type of data in the list.
    """

    # establish the upper and lower bounds of where the target can be located
    # where lower bound is the first item in the list and upper bound is the last item in the list
    lower_bound = 0
    upper_bound = len(list) - 1

    while lower_bound <= upper_bound:
        mid = (upper_bound + lower_bound) // 2

        if list[mid] < target:
            lower_bound = mid + 1

        elif list[mid] < target:
            upper_bound = mid - 1

        else:
            return mid

    # if we reach this point, the target value is not in the list. return None
    return None


def recursive_binary_search(list, low, high, target):

    # base case
    if high >= low:

        mid = (high + low) // 2

        if list[mid] == target:
            return mid # we found the target value
        
        elif list[mid] > target:
            return recursive_binary_search(list, low, mid -1, target)
        
        else:
            return recursive_binary_search(list, mid +1, high, target)
        
    else: # element not
        return None 