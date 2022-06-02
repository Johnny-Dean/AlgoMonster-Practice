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


# Given an array of integers sorted in increasing order and a target, find the index of the first element in the
# array that is larger than or equal to the target. Assume that it is guaranteed to find a satisfying number.

# INITIAL DRAFT
# def mod_binary_search(arr: List[int], target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] >= target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#     return -1
# Wrong because I did not read instructions thoroughly, find the FIRST occurence

def first_not_smaller(arr: List[int], target):
    left, right = 0, len(arr) - 1
    candidate = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            candidate = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    return candidate


# Given a sorted array of integers and a target integer, find the first occurrence of the target and return its
# index. Return -1 if the target is not in the array.
def find_first_occurence(arr: List[int], target):
    left, right = 0, len(arr) - 1
    candidate = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            candidate = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return candidate


# Given an integer, find its square root without using the built-in square root function. Only return the integer
# part (truncate the decimals).
def square_root(n: int):
    # If 0 return 0
    if n == 0:
        return 0
    # We don't need to create a pseudo array here with range, we can just treat the numbers from 1 - 9 to be our
    # array for us
    left, right = 1, n
    candidate = -1
    while left <= right:
        mid = (left + right) // 2
        # Found a potential candidate on the left side, so we can cut off anything from our mid
        # and move our boundary to one after it
        if mid * mid <= n:
            candidate = mid
            left = mid + 1
        # Landed somewhere where the values were greater than our target, so we adjust our boundary to exclude the
        # right and the ones after it
        else:
            right = mid - 1
    return candidate


# A sorted array of unique integers was rotated at an unknown pivot. For example, [10, 20, 30, 40, 50] becomes
# [30, 40, 50, 10, 20]. Find the index of the minimum element in this array. All the numbers are unique.
def find_min_rotated(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    candidate = -1
    while left <= right:
        mid = (left + right) // 2
        # -1 is last element of array
        if arr[mid] <= arr[-1]:
            candidate = mid
            # See if we can find smaller
            right = mid - 1
        else:
            left = mid + 1
    return candidate


# A mountain array is defined as an array that
#
# has at least 3 elements has an element with the largest value called "peak", with index k. The array elements
# monotonically increase from the first element to A[k], and then monotonically decreases from A[k + 1] to the last
# element of the array. Thus creating a "mountain" of numbers. That is, given A[0]<...<A[k-1]<A[k]>A[k+1]>...>A[n-1],
# we need to find the index k. Note that the peak element is neither the first nor the last element of the array.
#
# Find the index of the peak element. Assume there is only one peak element.
#
# Input: 0 1 2 3 2 1 0
#
# Output: 3
#
# Explanation: the largest element is 3 and its index is 3.

# Reduce the problem into an array of T or F
# We know a peak is the largest value that has a smaller value after it
# Check if our current element has a smaller value ahead of it, if it does its our current candidate
# Replace candidate if we find something larger
# Emphasis on only ONE peak, we may have an element thats greater than the one after it, but it would not be the largest
def peak_of_mountain_array(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    candidate = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            candidate = mid
            right = mid - 1
        else:
            left = mid + 1
    return candidate


if __name__ == '__main__':
    sorted_arr = [1, 2, 3, 4, 5]
    print("Binary search: ")
    print(binary_search(sorted_arr, 3))
    print(binary_search(sorted_arr, 69))
    bool_arr = [False, False, False, False, True, True, True, True]
    print("Find boundary using binary search concept:")
    print(find_boundary(bool_arr))
