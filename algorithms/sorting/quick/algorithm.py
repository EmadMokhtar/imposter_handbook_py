def quick_sort(unsorted_list):
    """
    Quick sort algorithm
    """
    if len(unsorted_list) < 2:
        return unsorted_list
    
    pivot_item = unsorted_list.pop(len(unsorted_list)-1)
    less_list = []
    greater_list =  []
    for item in unsorted_list:
        if item < pivot_item:
            less_list.append(item)
        elif item > pivot_item:
            greater_list.append(item)

    return quick_sort(less_list) + [pivot_item] + quick_sort(greater_list)
