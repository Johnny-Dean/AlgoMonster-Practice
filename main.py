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


if __name__ == '__main__':
    to_sort = [58, 2, 1003, 3, 4, 5, 23, 23, 21]
    insertion_sorted = insertion_sort(to_sort)
    print("Insertion Sorted: ")
    print(" ".join(map(str, insertion_sorted)))
    selection_sorted = selection_sort(to_sort)
    print("Selection Sorted:")
    print(" ".join(map(str, selection_sorted)))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
