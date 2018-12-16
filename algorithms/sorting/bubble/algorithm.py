def bubble_sort(unsorted_list):
    """
    Bubble sort algorithm
    """
    list_len = len(unsorted_list)
    for i in range(list_len):
        for j in range(0, list_len - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j + 1], unsorted_list[j] = (
                    unsorted_list[j],
                    unsorted_list[j + 1],
                )
    return unsorted_list
