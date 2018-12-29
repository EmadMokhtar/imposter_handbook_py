from math import floor


def binary_search(haystack, element):
    """
    Search for an element in the haystack using binary search
    :param haystack: container
    :param element: the element
    :return: `True` if the element in the haystack, otherwise `False`
    """
    start_index = 0
    end_index = len(haystack)
    while start_index < end_index:
        middle = (start_index + end_index) // 2
        if haystack[middle] == element:
            return True
        elif haystack[middle] < element:
            start_index = middle
        else:
            end_index = middle
    return False
