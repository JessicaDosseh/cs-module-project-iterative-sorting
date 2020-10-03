def linear_search(arr, target):
    # Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
    # If x matches with an element, return the index.
    # If x doesn’t match with any of elements, return -1
    for index, value in enumerate(arr):
        if value == target:
            print(index)
            return index

    return -1   # value not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here

    return -1  # not found


test_array = [12, 20, 8, 1, 6, 14, 29, 10, 2, 5]
linear_search(test_array, 6)
