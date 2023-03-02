def insertion_sort(list):
    ind_length = range(1, len(list))  # get the length as a list, so we can iterate through the unsorted list
    for i in ind_length:
        value = list[i]  # grab our value to work with

        while list[i - 1] > value and i > 0:  # while item to left of our value, is greater than the value
            list[i], list[i - 1] = list[i - 1], list[i]  # swap the values in the list
            i = i - 1

    return list


def insertion_sort_slightly_cleaner(list):
    for i in range(1, len(list)):
        value = list[i]
        while list[i - 1] > value and i > 0:
            list[i], list[i - 1] = list[i - 1], list[i]  # swap the values in the list
            i = i - 1

    return list
