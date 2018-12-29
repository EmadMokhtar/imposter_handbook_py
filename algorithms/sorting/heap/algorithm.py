def heap_sort(unsorted_list):
    """
    Heap sort algorithm
    """
    list_len = len(unsorted_list)

    # Build a maxheap from the list
    for i in range(list_len, -1, -1):
        heapify(unsorted_list, list_len, i)

    # One by one extract elements from the heap
    for i in range(list_len - 1, 0, -1):
        unsorted_list[i], unsorted_list[0] = unsorted_list[0], unsorted_list[i]
        heapify(unsorted_list, i, 0)

    return unsorted_list


def heapify(tree, root, initial_index):
    """
    Heapify a list/tree at an index `i`
    :param tree: Tree
    :param root: Root element
    :param initial_index: initial index
    :return: Max heap
    """
    largest = initial_index  # Initialize largest as root
    left = 2 * initial_index + 1  # left = 2*i + 1
    right = 2 * initial_index + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if left < root and tree[initial_index] < tree[left]:
        largest = left

    # See if right child of root exists and is
    # greater than root
    if right < root and tree[largest] < tree[right]:
        largest = right

        # Change root, if needed
    if largest != initial_index:
        tree[initial_index], tree[largest] = tree[largest], tree[initial_index]  # swap

        # Heapify the root.
        heapify(tree, root, largest)
