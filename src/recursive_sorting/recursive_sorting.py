# TO-DO: complete the helper function below to merge 2 sorted arrays
import random
testArray = [random.randint(1, 100) for _ in range(6)]
print("unsorted array", testArray)
# merge sort steps:
# split array into seperate sub arrays containing length == 1
# examine individual items, compare their values, merge into temp arr
# compare one array against the next and merge into new array (length i*2)


def merge(arrA, arrB):
    # starting at beginning of `a` and `b`
    # compare the next value of each
    # add smallest to `merged_arr`
    print("arrA and b", arrA, arrB)
    arrC = []
    # TO-DO
    # while a and b both contain anything:

    while len(arrB) and len(arrA):
        # if first arrA value is larger than arrB value, we want to do
        # print("aEl and bEl => ", aElements, bElements)
        print("first vals", arrA[0], arrB[0])
        if arrA[0] > arrB[0]:
            arrC.append(arrB[0])
            arrB.pop(0)
        else:
            arrC.append(arrA[0])
            arrA.pop(0)

    while len(arrA) and not len(arrB):
        arrC.append(arrA[0])
        arrA.pop(0)

    while len(arrB) and not len(arrA):
        arrC.append(arrB[0])
        arrB.pop(0)

    print("inside merge helper:", arrC)
    return arrC


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # recursively call merge_sort() on LHS
    # recursively call merge_sort() on RHS
    # merge sorted pieces
    if len(arr) == 1:
        return arr

    half = len(arr) // 2
    right = arr[half:]
    left = arr[:half]

    return merge(merge_sort(left), merge_sort(right))


print("merge sort:", merge_sort(testArray))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
