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


# There are n packages that needs to be transported from one city to another, and you need to transport them there
# within d days. For the ith package, the weight of the package is weights[i]. You are required to deliver them in
# order with a rental truck. The rental trucks come in different sizes. The bigger trucks have greater weight
# capacity but cost more to rent. To minimize cost, you want to deliver the packages in one truck once per day,
# with a weight capacity as small as possible to save on rental cost. What is the minimum weight capacity of the
# truck that is required to deliver all packages within d days?

def can_ship_in_time(weights: List[int], trial_max_weight: int, deadline: int) -> bool:
    # estimation of days to ship, we start with the assumption of one
    days_to_ship = 1
    # our load capacity starts at our max_weight which is currently a trial
    load_capacity = trial_max_weight
    # way to index throughout our entire array like a for loop
    i = 0
    upper_bound = len(weights)

    while i < upper_bound:
        # if our load_capacity can handle the current weight index then we subtract it from our load_capacity
        # and increment our pointer
        if load_capacity >= weights[i]:
            load_capacity -= weights[i]
            i += 1
        # else if it could not, we increase our days to ship and reset our load_capacity
        else:
            days_to_ship += 1
            load_capacity = trial_max_weight

    return days_to_ship <= deadline


def min_max_weight(weights: List[int], deadline: int) -> int:
    # We know at minimum our ship needs to be able to contain our largest weighted object
    min_ptr = max(weights)
    # We know at max the ship should be able to carry all the packagea in one day
    max_ptr = sum(weights)
    # the solution is somewhere in the middle, we need to find the boundary for it with binary search
    candidate = max_ptr
    while min_ptr <= max_ptr:
        # Find the middle of the min and max, since we know our answer is somewhere in the middle of the two
        # Our size of truck can be any arbitrary number
        middle = (min_ptr + max_ptr) // 2
        # We found a candidate but check if we can find one even smaller to save on costs
        if can_ship_in_time(weights, middle, deadline):
            candidate = middle
            max_ptr = middle - 1
        # It was not feasible, so we need to increase the weight capacity of our trucks
        else:
            min_ptr = middle + 1
    return candidate


# You've begun working in the one and only Umbristan. As part of your job working for the government you are asked to
# organize newspapers. Each morning your fellow coworkers will dilligently read through the newspapers carefully
# examining its contents. It is your job to organize the newspapers into piles and hand them out to your coworkers to
# read through. Each newspaper is assigned a time based on how much time it would take to read through its contents.
# The newspapers are carefully layed out in a line in a particular order that must not be broken when assigning the
# newspapers. That is you cannot pick and choose newspapers to make a pile to assign to a co-worker to read through.
# Instead you must take a particular subsection of the line of newspapers, make a pile and give that to a co-worker.
#
# What is the minimum amount of time it would take to have your coworkers go through all the newspapers?

# This is similar to our previous problem, except instead of a deadline we have number of coworkers
# We want to find the shortest amount of time we can split up the newspaper reading

def can_read_in_time(newspaper_read_times: List[int], coworkers: int, time_to_beat_or_equal: int):
    time_taken, coworkers_needed = 0, 0

    for read_time in newspaper_read_times:
        # if one single read time is greater than our time to beat then it is impossible to beat the time
        if read_time > time_to_beat_or_equal:
            return False
        # Split check, if our time take plus our current read leads to a larger read time then we need to split
        if time_taken + read_time > time_to_beat_or_equal:
            # "spawn" new coworker
            time_taken = 0
            coworkers_needed += 1
        time_taken += read_time
    # if we have leftover time that wasn't finished we need one more coworker
    if time_taken != 0:
        coworkers_needed += 1
    # we successfully beat or equalled the time, but did we do it with the right amount of coworkers we were given
    return coworkers_needed <= coworkers


def newspaper_split(newspaper_read_times: List[int], coworkers: int):
    # 1 <= newspapers.length <= 10^5
    low, high = 0, 1000000001

    while low <= high:
        middle = (low + high) // 2
        if can_read_in_time(newspaper_read_times, coworkers, middle):
            high = middle - 1
        else:
            low = middle + 1
    return high + 1


if __name__ == '__main__':
    sorted_arr = [1, 2, 3, 4, 5]
    print("Binary search: ")
    print(binary_search(sorted_arr, 3))
    print(binary_search(sorted_arr, 69))
    bool_arr = [False, False, False, False, True, True, True, True]
    print("Find boundary using binary search concept:")
    print(find_boundary(bool_arr))
