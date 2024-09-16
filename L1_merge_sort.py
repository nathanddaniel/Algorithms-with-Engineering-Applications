import numpy as np
import random
import time

N = 80000

# Define array
arr = np.array([0] * N)


def merge(A, p, q, r):
    # Copy the left and right sublists/subarrays.
    # If A is a list, slicing creates a copy.
    if type(A) is list:
        left = A[p: q + 1]
        right = A[q + 1: r + 1]
    # Otherwise a is a np.array, so create a copy with list().
    else:
        left = list(A[p: q + 1])
        right = list(A[q + 1: r + 1])

    i = 0  # index into left sublist/subarray
    j = 0  # index into right sublist/subarray
    k = p  # index into a[p: r+1]

    # Combine the two sorted sublists/subarrays by inserting into A
    # the lesser exposed element of the two sublists/subarrays.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1

    # After going through the left or right sublist/subarray, copy the
    # remainder of the other to the end of the list/array.
    if i < len(left):  # copy remainder of left
        A[k: r + 1] = left[i:]
    if j < len(right):  # copy remainder of right
        A[k: r + 1] = right[j:]


def merge_sort(A, p=0, r=None):

    # If r is not given, set to the index of the last element of the list/array.
    if r is None:
        r = len(A) - 1
    if p >= r:  # 0 or 1 element?
        return
    q = (p + r) // 2  # midpoint of A[p: r]
    merge_sort(A, p, q)  # recursively sort A[p: q]
    merge_sort(A, q + 1, r)  # recursively sort A[q+1: r]
    merge(A, p, q, r)  # merge A[p: q] and A[q+1: r] into A[p: r]


def print_list(A, n):
    for i in range(0, N):
        print(" %3d" % (A[i]), end="")
    print()


def main():
    for i in range(0, N):
        arr[i] = random.randint(0, 10*N)

    print("START PROGRAM")
    print("LIST BEFORE MERGE SORT")
    #print_list(arr, N)
    t0 = time.time()

    print("LIST AFTER MERGE SORT")
    merge_sort(arr)
    #print_list(arr, N)
    t1 = time.time()

    print(t1-t0)


if __name__ == "__main__":
    main()