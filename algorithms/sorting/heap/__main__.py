from algorithm import heap_sort


unsorted_list = [23, 4, 42, 15, 16, 8]
print('Unsorted list')
print(unsorted_list)
sorted_list = heap_sort(unsorted_list)
print("Sorted list")
print(sorted_list)