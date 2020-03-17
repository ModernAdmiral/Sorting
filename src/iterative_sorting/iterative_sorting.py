import random
testArray = [random.randint(1, 100) for _ in range(20)]
print("unsorted array", testArray)

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        cur_min = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_min, len(arr)):
            if (arr[cur_min] > arr[j]):  # scan for smaller number than current
                # if you find one, set the CURRENT INDEX to be the new "current smallest number's INDEX"
                cur_min = j  # BLOCKER! YOU ONLY DEAL WITH INDEX HERE

        # TO-DO: swap
        # we will swap the value of current index with the value of cur_min.
        temp = arr[cur_index]
        arr[cur_index] = arr[cur_min]
        arr[cur_min] = temp

    return arr


print("selection sort", selection_sort(testArray))


# TO-DO:  implement the Bubble Sort function below
# if
def bubble_sort(arr):
    # this one was pretty straight forward
    for i in arr:
        for j in range(0, len(arr) - 1):
            if (arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


print("bubble sort", bubble_sort(testArray))
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
