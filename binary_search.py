from typing import List


def binary_search(arr: List[int], target: int):
    left, right = 0, len(arr) - 1
    # The equality is for the chance of a one element loop, if we are given a one element array we would miss it
    while left <= right:
        mid = (left + right) // 1
        if arr[mid] == target:
            return mid
        # If our arr at middle is greater than our target, in a sorted array we know we can reduce our search to
        # everything below middle
        elif arr[mid] > target:
            right = mid - 1
        # If our arr at middle is less than our target, in a sorted array we know we can reduce our search to
        # everything above middle
        elif arr[mid] < target:
            left = mid + 1
    # If we break the loop we never found our element
    return -1


# An array of boolean values is divided into two sections; the left section consists of all false and the right
# section consists of all true. Find the boundary of the right section, i.e. the index of the first true element. If
# there is no true element, return -1.
def find_boundary(arr: List[bool]) -> int:
    # Get our index
    left, right = 0, len(arr) - 1
    leftmost_true_index = -1
    # Binary search
    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            leftmost_true_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return leftmost_true_index


if __name__ == '__main__':
    sorted_arr = [1, 2, 3, 4, 5]
    print("Binary search: ")
    print(binary_search(sorted_arr, 3))
    print(binary_search(sorted_arr, 69))
    bool_arr = [False, False, False, False, True, True, True, True]
    print("Find boundary using binary search concept:")
    print(find_boundary(bool_arr))
