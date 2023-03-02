
def merge_sort(list):
    if len(list) > 1:
        left_split = list[:len(list) // 2]
        right_split = list[len(list) // 2:]

        merge_sort(left_split)
        merge_sort(right_split)

        i = 0  # left list index
        j = 0  # right list index
        k = 0  # merged list index
        while i < len(left_split) and j < len(right_split):
            if left_split[i] < right_split[j]:
                list[k] = left_split[i]
                i += 1
            else:
                list[k] = right_split[j]
                j += 1
            k += 1

        while i < len(left_split):
            list[k] = left_split[i]
            i += 1
            k += 1

        while j < len(right_split):
            list[k] = right_split[j]
            j += 1
            k += 1

    return list
