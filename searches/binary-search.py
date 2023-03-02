
def binary_search(list, target):
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
    upper_bound = len(list) + 1

    #
    while lower_bound <= upper_bound:
        middle = (upper_bound + lower_bound) / 2
        # establish out middle position in the list.
        midpoint = list[middle] 

        # if midpoint is our target valiue, return midpoint
        if midpoint == target:
            return midpoint
        
        # if target is less than midpoint, set our new upper bound to this midpoint - 1
        elif target < midpoint:
            upper_bound = midpoint - 1

        # if target is greater than midpoint, set our new lower bound to this midpoint + 1
        else:
            lower_bound = midpoint + 1

    # if we reach this point, the target value is not in the list. return None
    return None