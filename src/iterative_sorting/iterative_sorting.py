# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for unsorted_index in range(cur_index + 1, len(arr)):
            if arr[unsorted_index] < arr[smallest_index]:
                smallest_index = unsorted_index

        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    print(f'selection_sort: {arr}')
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # declaration
    end_of_list = len(arr)
    current_index = 0
    # TO-DO:
    # Compare the first and second item of the data list.
    # If the first item is bigger than the second item, swap the items.
    for i in range(len(arr)):
        # TO-DO:
        # Move to the next item.
        # Compare the second item with the third item.
        # If the second item is bigger than the third, swap the items.
        for compare in range(current_index + 1, end_of_list):

            if arr[current_index] > arr[compare]:
                # [ > ] ascending order --- [ < ] descending order
                arr[current_index], arr[compare] = arr[compare], arr[current_index]
                current_index += 1

            else:
                current_index += 1

        # Do this for every item until the end of the list.
        # Repeat steps 1-3 (decrementing “the end of the list” by 1 each time).
        end_of_list -= 1
        current_index = 0

    print(f'bubble_sort: {arr}')
    return arr


test_array = [12, 20, 8, 1, 6, 14, 29, 10, 2, 5]
selection_sort(test_array)
bubble_sort(test_array)


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
