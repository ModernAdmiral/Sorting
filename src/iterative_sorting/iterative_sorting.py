# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        cur_min = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr) - 1):
            if (arr[cur_index] > arr[j]):  # scan for smaller number than current
                cur_min = j  # if you find one, set it to be the new "current smallest number"
                print("in nested loop", cur_index, cur_min)

        # TO-DO: swap
        # we will swap the current index with the cur_min
    temp = arr[cur_index]
    arr[cur_index] = arr[cur_min]
    arr[cur_min] = temp
    print("in outer loop", cur_min, cur_index)

    return arr


print(selection_sort([2, 8, 5, 3, 9, 4, 1]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
