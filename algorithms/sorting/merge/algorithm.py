def merge_sort(unsorted_list):
    """
    Merge sort algorithm
    """
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    middle = len(unsorted_list)//2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    return _merge(merge_sort(left_list), merge_sort(right_list))


def _merge(left_list, right_list):
    """
    Merge two lists and apply the sorting
    """
    sorted_list = []
    while left_list or right_list:
        if left_list and right_list:
            if left_list[0] < right_list[0]:
                sorted_list.append(left_list.pop(0))
            else:
                sorted_list.append(right_list.pop(0))
        elif left_list:
            sorted_list.append(left_list.pop(0))
        elif right_list:
            sorted_list.append(right_list.pop(0))
    return sorted_list
