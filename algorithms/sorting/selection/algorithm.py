def selection_sort(unsorted_list):
    list_length = len(unsorted_list)
    for i in range(list_length):
        current_min_index = i
        for x in range(i+1, list_length):
            if unsorted_list[x] < unsorted_list[current_min_index]:
                current_min_index = x

        if current_min_index != i:
            unsorted_list[i], unsorted_list[current_min_index] = unsorted_list[current_min_index], unsorted_list[i]
        
    return unsorted_list
