from typing import List


def insertion_sort(arr: List[int]):
    for i, element in enumerate(arr):
        curr_index = i
        # Already consider the first element sorted
        # Check if curr_index is not out of range
        # Check that the element [curr_index - 1] is not larger than the element [curr_index]
        # If it is swap, else decrement curr_index
        while curr_index > 0 and arr[curr_index] < arr[curr_index - 1]:
            # Swap
            arr[curr_index], arr[curr_index - 1] = arr[curr_index - 1], arr[curr_index]
            curr_index -= 1
    return arr


def selection_sort(arr: List[int]):
    # Find the upper index of our array.
    upper_bound = len(arr)

    for i in range(upper_bound):
        min_index = i
        # Find smallest element in the rest of the array (anything before I is sorted).
        for j in range(i, upper_bound):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def bubble_sort(arr: List[int]):
    upper_bound = len(arr)
    # Integers are not iterable, we have to use a reversed range to get 8 - 0 for our indices.
    # C++: for (int i = arr.size(); i > 0; i--)
    # We start from 8 because our inner loop bubbles up elements to this index, as i decrements we can assume
    # That anything greater than i (in range) is sorted
    for i in reversed(range(upper_bound)):
        # If a swap was not needed the array is sorted, so we can return
        swap_occurred = False
        # Bubble up from our current index to the last sorted element
        # i's index will be one less than the last sorted element's index
        # C++:  for (int j = 0; j < i; j++)
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_occurred = True
        if not swap_occurred:
            return arr
    return arr


if __name__ == '__main__':
    for_selection_sort = [58, 2, 1003, 3, 4, 5, 23, 23, 21]
    for_insertion_sort = [58, 2, 1003, 3, 4, 5, 23, 23, 21]
    for_bubble_sort = [58, 2, 1003, 3, 4, 5, 23, 23, 21]

    insertion_sorted = insertion_sort(for_insertion_sort)
    print("Insertion Sorted: ")
    print(" ".join(map(str, insertion_sorted)))

    selection_sorted = selection_sort(for_selection_sort)
    print("Selection Sorted:")
    print(" ".join(map(str, selection_sorted)))

    bubble_sorted = bubble_sort(for_bubble_sort)
    print("Bubble Sorted: ")
    print(" ".join(map(str, bubble_sorted)))
