def linear_search(arr, target):
    # Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
    # If x matches with an element, return the index.
    # If x doesn’t match with any of elements, return -1
    for index, value in enumerate(arr):
        if value == target:
            print(f'linear_search: {index}')
            return index

    return -1   # value not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Compare x with the middle element.
    # If x matches with middle element, we return the mid index.
    # Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
    # Else (x is smaller) recur for the left half.

    # declaration
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2  # integer division

        if arr[middle] == target:  # Check if x is present at mid
            print(f'binary_search: {middle}')
            return middle
        elif arr[middle] < target:  # If x is greater, ignore left half
            left = middle + 1
        else:
            right = middle - 1  # If x is smaller, ignore right half

    return -1  # value not found


test_array = [12, 20, 8, 1, 6, 14, 29, 10, 2, 5]
linear_search(test_array, 6)
binary_search(test_array, 6)
